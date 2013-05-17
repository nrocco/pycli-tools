# -*- coding: utf-8 -*-

def ask_user_yesno(message='Are you sure you want to continue?',
                   yes_on_enter=True, yes='y', no='n'):
    '''
    Helper function that wraps python's :py:func:`read_input()` function.

    Use this if your program should rely on simple user input like
    asking for confirmation to continue.

    Possible answers are `yes` or `no`. You can also specify the default
    answer to take if the user provides no input.

    **Arguments:**

        `message`
            The question you want to display.
        `yes_on_enter`
            The default action to take when the user provides no input
            (e.g. just presses [enter]).
        `yes`
            Letter to use for a positive answer.
        `no`
            Letter to use for a negative answer.

    **Returns:**

        `True` if the user answers positively, `False` otherwise.
    '''
    if yes_on_enter:
        default_answer = True
        line = '%s [%s/%s] ' % (message, yes.upper(), no)
    else:
        default_answer = False
        line = '%s [%s/%s] ' % (message, yes, no.upper())

    try:
        while True:
            answer = raw_input(line).lower()
            if answer == '':
                return default_answer
            elif answer[0] == yes:
                return True
            elif answer[0] == no:
                return False
    except KeyboardInterrupt:
        return False
