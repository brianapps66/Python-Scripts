import argparse
import re
import sys

parser = argparse.ArgumentParser(
    description="""unique_characters checks if a string contains all unique
                    characters.
                    It uses a regular expression to see if any characters
                    repeat and it returns a boolean."""
)
parser.add_argument('string', help="""The string to check.
                                   If there are spaces then surround the
                                   argument with inverted commas.""")
args = parser.parse_args()


def check_characters(arg):
    regex = r'^.*(.).*\1.*$'
    boo = re.findall(regex, arg)
    if len(boo) >= 1:
        return False
    else:
        return True


print(check_characters(sys.argv[1]))
