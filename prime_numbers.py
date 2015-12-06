from itertools import count, islice
import argparse
import sys


parser = argparse.ArgumentParser(
    description="""prime_numbers takes a single int argument n and returns
                    the nth prime number"""
)
parser.add_argument('int', help="""The index of the prime number to return""")
args = parser.parse_args()


def prime(x):
    primes = (x for x in count(2) if all(x % d for d in range(2, x)))
    return next(islice(primes, x-1, x))

print(prime(int(sys.argv[1])))
