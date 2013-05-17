import os
import sys

from pycli_tools import rawinput



def test_default_yes_yes():
    def raw_input_mock(prompt):
        return 'y'
    rawinput.raw_input = raw_input_mock
    assert True == rawinput.ask_user_yesno()


def test_default_yes_no():
    def raw_input_mock(prompt):
        return 'n'
    rawinput.raw_input = raw_input_mock
    assert False == rawinput.ask_user_yesno()


def test_default_yes_empty():
    def raw_input_mock(prompt):
        return ''
    rawinput.raw_input = raw_input_mock
    assert True == rawinput.ask_user_yesno()


def test_default_no_yes():
    def raw_input_mock(prompt):
        return 'y'
    rawinput.raw_input = raw_input_mock
    assert True == rawinput.ask_user_yesno(yes_on_enter=False)


def test_default_no_no():
    def raw_input_mock(prompt):
        return 'n'
    rawinput.raw_input = raw_input_mock
    assert False == rawinput.ask_user_yesno(yes_on_enter=False)


def test_default_no_empty():
    def raw_input_mock(prompt):
        return ''
    rawinput.raw_input = raw_input_mock
    assert False == rawinput.ask_user_yesno(yes_on_enter=False)


def test_continue():
    def raw_input_mock(prompt):
        return 'c'
    rawinput.raw_input = raw_input_mock
    assert True == rawinput.ask_user_yesno(yes='c', no='a')


def test_abort():
    def raw_input_mock(prompt):
        return 'a'
    rawinput.raw_input = raw_input_mock
    assert False == rawinput.ask_user_yesno(yes='c', no='a')

def test_ctrl_c():
    def raw_input_mock(prompt):
        raise KeyboardInterrupt()
    rawinput.raw_input = raw_input_mock
    assert False == rawinput.ask_user_yesno()
