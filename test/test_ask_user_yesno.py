import os
import sys

import pycli_tools



def test_default_yes_yes():
    def raw_input_mock(prompt):
        return 'y'
    pycli_tools.raw_input = raw_input_mock
    assert True == pycli_tools.ask_user_yesno()


def test_default_yes_no():
    def raw_input_mock(prompt):
        return 'n'
    pycli_tools.raw_input = raw_input_mock
    assert False == pycli_tools.ask_user_yesno()


def test_default_yes_empty():
    def raw_input_mock(prompt):
        return ''
    pycli_tools.raw_input = raw_input_mock
    assert True == pycli_tools.ask_user_yesno()


def test_default_no_yes():
    def raw_input_mock(prompt):
        return 'y'
    pycli_tools.raw_input = raw_input_mock
    assert True == pycli_tools.ask_user_yesno(yes_on_enter=False)


def test_default_no_no():
    def raw_input_mock(prompt):
        return 'n'
    pycli_tools.raw_input = raw_input_mock
    assert False == pycli_tools.ask_user_yesno(yes_on_enter=False)


def test_default_no_empty():
    def raw_input_mock(prompt):
        return ''
    pycli_tools.raw_input = raw_input_mock
    assert False == pycli_tools.ask_user_yesno(yes_on_enter=False)


def test_continue():
    def raw_input_mock(prompt):
        return 'c'
    pycli_tools.raw_input = raw_input_mock
    assert True == pycli_tools.ask_user_yesno(yes='c', no='a')


def test_abort():
    def raw_input_mock(prompt):
        return 'a'
    pycli_tools.raw_input = raw_input_mock
    assert False == pycli_tools.ask_user_yesno(yes='c', no='a')
