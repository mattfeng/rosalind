#!/usr/bin/env python
"""
rna.py

Translates a DNA string into RNA.
"""

import argparse

def main(fname):
    with open(fname) as f:
        dna = f.read().strip()

    table = str.maketrans("T", "U")
    print(dna.translate(table))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file",
        )

    args = parser.parse_args()

    main(args.fname)
