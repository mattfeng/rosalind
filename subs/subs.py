#!/usr/bin/env python

"""
subs.py

Finding a motif in DNA
======================
The key algorithm to use to achieve O(n + m) running time is Rabin-Karp.
"""

import argparse

def rabinkarp(pat, text):
    """Find all occurrences of `pat` in `text` using Rabin-Karp.

    :param str pat: pattern to find within text.
    :param str text: text within which to search for pat.
    :return: a list of indices of the occurrence of `pat` in `text`.
    :rtype: List[int]
    """

    p = 31
    m = int(1e9 + 9)
    s, t = len(pat), len(text)

    # pre-compute the powers that will be used as coefficients
    pows = [1] * max(s, t)
    for i in range(1, len(pows)):
        pows[i] = (pows[i - 1] * p) % m

    # compute prefix hashes
    preh = [0]
    for i in range(0, t):
        h = (preh[-1] + ord(text[i]) * pows[i]) % m
        preh.append(h)

    # compute pattern hash
    path = 0
    for i in range(0, s):
        path = (path + ord(pat[i]) * pows[i]) % m

    # find occurrences
    locs = []
    for i in range(0, t - s + 1):
        cur_h = (preh[i + s] - preh[i]) % m

        if (path * pows[i]) % m == cur_h:
            locs.append(i)

    return locs


def main(fname):

    with open(fname) as f:
        text = f.readline().strip()
        pat = f.readline().strip()

    indices = rabinkarp(pat, text)

    for i in indices:
        print(i + 1, end=" ")

    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file"
        )

    args = parser.parse_args()

    main(args.fname)
