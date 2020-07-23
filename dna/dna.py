#!/usr/bin/env python

from collections import Counter
import argparse

def main(fname):
    with open(fname) as f:
        seq = f.read().strip()

    counts = Counter(seq)
    for c in "ACGT":
        print(f"{counts[c]}", end=" ")
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to DNA sequence to count",
        )

    args = parser.parse_args()

    main(args.fname)


