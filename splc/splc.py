#!/usr/bin/env python

"""
splc.py


RNA Splicing
============

"""

from biology.fasta import read_fasta
from biology.sequence import r2p

import argparse

def rna_splice(dnaseq, dnasubseqs):
    for ss in dnasubseqs:
        dnaseq = dnaseq.replace(ss, "")

    trns = str.maketrans("ACGT", "ACGU")

    return dnaseq.translate(trns)

def main(fname):
    with open(fname) as f:
        seqs = read_fasta(f)

    fasta_seqs = list(seqs.items())
    dnaseq = fasta_seqs[0][1]
    dnasubseqs = [seq for _, seq in fasta_seqs[1:]]

    rna = rna_splice(dnaseq, dnasubseqs)

    print(r2p(rna))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file"
        )

    args = parser.parse_args()

    main(args.fname)
