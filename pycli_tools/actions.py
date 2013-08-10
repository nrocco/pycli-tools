from argparse import Action
from os.path import isfile, isabs, abspath


class ExistingFileAction(Action):
    def __call__(self, parser, args, values, option_string=None):
        if not isfile(values):
            parser.error('File `%s` does not exist' % values)

        path = values if isabs(values) else abspath(values)
        setattr(args, self.dest, path)
