"""
revc.py

(Reverse) complementing a strand of DNA.
"""

import argparse

def main(fname):
    with open(fname) as f:
        seq = f.read().strip()

    table = str.maketrans("ATCG", "TAGC")
    revc = seq[::-1].translate(table)

    print(revc)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file",
        )

    args = parser.parse_args()

    main(args.fname)
