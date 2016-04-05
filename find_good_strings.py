import re

file = open('good_or_bad_strings.txt', 'r').read().splitlines()
vowels = ['a', 'e', 'i', 'o', 'u']
def first_rule():
    count = 0
    for line in file:
        if re.match(r'.*([aeiou].*){3,}',line):
            if re.match(r'.*([a-z])\1.*', line):
                if not re.match(r'.*(ab|cd|pq|xy).*', line):
                    count = count + 1
    print(count)

print(len([x for x in file if re.search("((a|e|i|o|u).*){3,}", x) and
           re.search("(""\w)\\1", x) and not re.search("ab|cd|pq|xy", x)]))


def second_rule():
    count = 0
    for line in file:
        if re.match(r'.*([a-z][a-z]).*\1.*',line):
            if re.match(r'.*([a-z]).{1}\1.*', line):
                count = count + 1
    print(count)

print(len([x for x in file if re.search("(\w\w).*\\1", x) and re.search("(""\w).\\1", x)]))

first_rule()
second_rule()
