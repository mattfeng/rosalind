#!/usr/bin/env python

"""
grph.py

Overlaps graphs
===============

"""

from biology.fasta import read_fasta
from collections import defaultdict

import argparse

def build_overlap_graph(dnaseqs, k):
    prefix_seqs = defaultdict(list)
    suffix_seqs = defaultdict(list)

    adj_list = defaultdict(list)

    for name, seq in dnaseqs.items():
        prefix = seq[:k]
        suffix = seq[-k:]
        prefix_seqs[prefix].append(name)
        suffix_seqs[suffix].append(name)

    for name, seq in dnaseqs.items():
        prefix = seq[:k]
        suffix = seq[-k:]

        for oname in prefix_seqs[suffix]:
            if oname != name:
                adj_list[name].append(oname)

    return adj_list

def main(fname):
    with open(fname) as f:
        dnaseqs = read_fasta(f)

    overlap_graph = build_overlap_graph(dnaseqs, 3)

    for name, adjnames in overlap_graph.items():
        for adjname in adjnames:
            print(name, adjname)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file"
        )

    args = parser.parse_args()

    main(args.fname)
