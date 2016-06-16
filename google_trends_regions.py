import csv
import re

# Enter the address of the CSV file downloaded from Google Trends
csv_file =
s = ''
d = {}

# This function converts the region data from the CSV file into a dictionary
def csv_to_dict(c):
    with open(c) as f:
        first = f.readline()
        name = re.match('Web Search interest: (.+)',first).group(1)
        d[name] = {}
        reader = csv.reader(f)
        for row in reader:
            if re.search(r'Region', str(row)):
                for i, line in enumerate(f):
                    if re.search(r'^\s*$',line):
                        break
                    matches = re.match(r'(.+),(.+)', line)
                    d[name][matches.group(1)] = int(matches.group(2))

# Returns every country in the dictionary
def get_all_countries(h):
    l = []
    for x in h:
        for y in h[x]:
            if y not in l:
                l.append(y)
    return l

# Prints the dictionary in a readable format
def print_dict(h):
    for x in h:
        print(x)
        [print(key, ':', value) for (key, value) in sorted(h[x].items(), key=lambda
            y: y[1], reverse = True)]
        print('\n')

# When working with more than one CSV file, this function will check if there
# are any countries from one file which are not in another file. It will
# append these countries to the dictionary with a value of zero so that every
# search term will have the same number of countries associated with it. This
# can be helpful when working with sorting algorithms, for example
def filler_countries(h):
    all_countries = get_all_countries(h)
    for x in h:
        countries = []
        for y in h[x]:
            print(y)
            countries.append(y)
        for z in all_countries:
            if z not in countries:
                h[x][z] = 0
    print("\n")

csv_to_dict(csv_file)

print_dict(d)

print(get_all_countries(d))

filler_countries(d)

print_dict(d)