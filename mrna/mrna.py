"""
mrna.py

Inferring mRNA from Protein
===========================

"""

from biology.constants import prot2rna
from collections import defaultdict

import argparse

def main(fname):
    with open(fname) as f:
        seq = f.readline().strip()

    ans = 3 # account for the stop codon
    for aa in seq:
        ans *= len(prot2rna[aa])
        ans %= 1000000

    print(ans)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file"
    )

    args = parser.parse_args()

    main(args.fname)
