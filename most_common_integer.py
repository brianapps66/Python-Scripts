"""Returns the most common integer in a list"""

import sys

def most_common_integer(l):
    return max(set(l), key=l.count)

print(most_common_integer(sys.argv[1].split(',')))
