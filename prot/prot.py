#!/usr/bin/env python

from biology.constants import rna2prot

import argparse

def main(fname):
    prot_seq = ""

    with open(fname) as f:
        seq = f.read().strip()
        for i in range(0, len(seq), 3):
            next_aa = rna2prot[seq[i:i+3]]

            if next_aa == "Stop":
                break

            prot_seq += next_aa

    print(prot_seq)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file"
        )

    args = parser.parse_args()

    main(args.fname)
