#!/usr/bin/env python

"""
fib.py

Rabbits and recurrence relations (dynamic programming).

Beginning with 1 pair of rabbits (at month 1), if every pair of rabbits produces
k pairs of rabbits each month, how many pairs of rabbits will exist after n months?

The second term is how many new offspring there are, which is determined
by the number of adult pairs (that is, two months ago).

F1 = 1
F2 = 1
F3 = F2 + F1 * k
F4 = F3 + F2 * k 
Fn = Fn-1 + Fn-2 * k
"""

import argparse

def main(num_months, num_pairs):
    # n = num_months
    # k = num_pairs

    num_rabbits = [0, 1, 1] # Let num_rabbits[0] be a dummy value.
    num_rabbits += [0] * (num_months - 2)

    for n in range(3, num_months + 1):
        num_rabbits[n] = num_rabbits[n - 1] + num_rabbits[n - 2] * num_pairs

    print(num_rabbits[num_months])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("num_months",
        help="number of months to solve for",
        type=int
        )

    parser.add_argument("num_pairs",
        help="number of pairs of offspring per adult rabbit pair",
        type=int
        )

    args = parser.parse_args()

    main(args.num_months, args.num_pairs)
