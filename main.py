"""ccwc command line tool

This script interprets several combinations of ccwc commands and outputs to the command
line result of such interpretation.

It is an exercise focused on wc command line tool challenge by John Crickett at
https://codingchallenges.fyi/challenges/challenge-wc/.
"""

import re
import ccwc_methods

ccwc = ccwc_methods.CCWC()

# A dictionary of ccwc command combinations with keys given as regex strings.
patterns = {
    r'^ccwc .+$': {
        r'^ccwc \w+\.\w+$': 'ccwc.ccwc_generic(file_name)',
        r'^ccwc -c \w+\.\w+$': 'ccwc.bytes_in_file(file_name)',
        r'^ccwc -l \w+\.\w+$': 'ccwc.lines_in_file(file_name)',
        r'^ccwc -w \w+\.\w+$': 'ccwc.words_in_file(file_name)',
        r'^ccwc -m \w+\.\w+$': 'ccwc.chars_in_file(file_name)',
    },
    r'^cat .+$': {
        r'^cat \w+\.\w+$': 'ccwc.st_output(file_name)',
        r'^cat \w+\.\w+ \| ccwc$': 'ccwc.ccwc_generic(file_name)',
        r'^cat \w+\.\w+ \| ccwc -[clmw]$': {
            r'^cat \w+\.\w+ \| ccwc -c$': 'ccwc.bytes_in_file(file_name)',
            r'^cat \w+\.\w+ \| ccwc -l$': 'ccwc.lines_in_file(file_name)',
            r'^cat \w+\.\w+ \| ccwc -w$': 'ccwc.words_in_file(file_name)',
            r'^cat \w+\.\w+ \| ccwc -m$': 'ccwc.chars_in_file(file_name)',
        }
    }
}


def apply_wc(action, file_name, search_object):
    """Searches through search_object keys for a match to the action.
    If match found, evaluates the value, which is a ccwc command and prints
    out the result.

    Parameters
    ----------
    action: string
        The value of the user input.
    file_name: string
        The name of the file.
    search_object: dict
        The object containing different representations of ccwc command.
    """
    if isinstance(search_object, dict):
        for key in search_object.keys():
            if re.match(key, action):
                apply_wc(action, file_name, search_object[key])
    elif isinstance(search_object, str):
        result = eval(search_object)
        print(' ', result, file_name)


def work_on_command(action):
    """Searches for a word combination given as word.word, if found, calls
    apply_wc function.

    Parameters
    ----------
    action: string
        The representation of the command typed in by the user.
    """
    file_name_regex = r'\b\w+\.\w+\b'
    file_name = re.findall(file_name_regex, action)
    if file_name:
        apply_wc(action, file_name[0], patterns)


if __name__ == '__main__':
    user_input = ''

    # To end the loop, type in exit.
    while user_input != 'exit':
        user_input = input(">")
        work_on_command(user_input)
