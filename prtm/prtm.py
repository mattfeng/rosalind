#!/usr/bin/env python

"""
prtm.py

Calculating protein mass
========================
"""

from biology.constants import amino2mass

import argparse

def main(fname):
    prot = open(fname).read().strip()

    weight = 0
    for aa in prot:
        weight += amino2mass[aa]

    print(weight)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file",
        )

    args = parser.parse_args()

    main(args.fname)
