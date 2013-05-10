import logging
import sys
from os import path

from argparse import ArgumentParser



log = logging.getLogger(__name__)


class ArgumentSuperParser(ArgumentParser):

    opt_config  = ('-c', '--config',  'path to the config file')
    opt_verbose = ('-v', '--verbose', 'output more verbose')
    opt_quiet   = ('-q', '--quiet',   'surpress all output')
    opt_version = ('-V', '--version', '%(prog)s ')

    def __init__(self, prog, version, default_config=None, *args, **kwargs):
        self._prog = prog
        self._version = version
        self._default_config_file = default_config

        self._main = self.get_main_parser(self._prog)
        self._main_argv, self._remaining_argv = self._main.parse_known_args()

        if self._main_argv.quiet:
            self._loglevel = 100
        else:
            self._loglevel = max(30 - self._main_argv.verbose * 10, 10)

        logging.basicConfig(level=self._loglevel, format='%(message)s')

        self._config_file = self._main_argv.config_file

        if self._config_file:
            if path.isfile(self._config_file):
                log.info('Reading default configuration from %s', self._config_file)
                from ConfigParser import ConfigParser
                self._config = self.get_config_parser(self._config_file)
                self._defaults = self.parse_config_defaults(self._config, self._prog)
            else:
                log.debug('Ignoring non-existent config file: %s', self._config_file)
                self._config = None
                self._defaults = {}
        else:
            self._config = None
            self._defaults = {}


        obj = super(ArgumentSuperParser, self).__init__(prog=self._prog, parents=[self._main], *args, **kwargs)

        self.add_opt_version(self._version, self)
        self.set_defaults_for_parser(self, self._defaults)

        return obj


    def get_main_parser(self, prog):
        mp = ArgumentParser(prog=prog, add_help=False)
        self.add_opt_config(mp)
        self.add_opt_verbose(mp)
        self.add_opt_quiet(mp)
        return mp


    def get_config_parser(self, file):
        config = ConfigParser()
        config.read(path.expanduser(file))
        return config


    def parse_config_defaults(self, parser, section):
        if parser.has_section(section):
            return dict(parser.items(section))
        else:
            log.debug('Section %s not found. Ignoring.', section)
            return {}


    def add_opt_config(self, parser):
        o = self.opt_config
        parser.add_argument(o[0], o[1], help=o[2], dest='config_file',
                            default=self._default_config_file)


    def add_opt_verbose(self, parser):
        o = self.opt_verbose
        parser.add_argument(o[0], o[1], default=0, action='count', help=o[2])


    def add_opt_quiet(self, parser):
        o = self.opt_quiet
        parser.add_argument(o[0], o[1], action='store_true', help=o[2])


    def add_opt_version(self, version, parser):
        v = self.opt_version
        parser.add_argument(v[0], v[1], action='version', version=v[2] + version)


    def set_defaults_for_parser(self, parser, defaults):
        parser.set_defaults(verbose=self._main_argv.verbose,
                            quiet=self._main_argv.quiet, **defaults)


    def parse_args(self, *args, **kwargs):
        self._args = super(ArgumentSuperParser, self).parse_args(self._remaining_argv)
        return self._args
