#!/usr/bin/env python

"""
hamm.py

Counting point mutations
========================

"""

import argparse

def hamming(s, t):
    dist = 0
    for a, b in zip(s, t):
        if a != b:
            dist += 1
    return dist

def main(fname):
    with open(fname) as f:
        seq1 = f.readline().strip()
        seq2 = f.readline().strip()

    print(hamming(seq1, seq2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file",
        )

    args = parser.parse_args()

    main(args.fname)
