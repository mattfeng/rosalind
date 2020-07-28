#!/usr/bin/env python

"""
cons.py

Consensus and Profile
=====================


"""

from biology.fasta import read_fasta
from collections import Counter

import argparse

def build_consensus_string(prof_matrix):
    consensus = ""
    for counts in prof_matrix:
        consensus += counts.most_common(1)[0][0]

    return consensus
    

def build_profile_matrix(seqs, symbs):
    pos_counts = []

    for letters in zip(*seqs):
        c = Counter(letters)
        pos_counts.append(c)

    return pos_counts


def main(fname):
    with open(fname) as f:
        fasta_strs = read_fasta(f)

    symbs = {
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3
        }

    mat = build_profile_matrix(fasta_strs.values(), symbs)
    cons = build_consensus_string(mat)

    print(cons)

    for symb in "ACGT":
        print(f"{symb}:", end="")
        for i in range(0, len(mat)):
            print(f" {mat[i][symb]}", end="")
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file"
        )

    args = parser.parse_args()

    main(args.fname)
