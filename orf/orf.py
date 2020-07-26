#!/usr/bin/env python

from biology.sequence import dna2rna, reverse_comp
from biology.constants import rna2prot
from biology.fasta import read_fasta

import argparse

def find_all_orfs(rnaseq, offsets=(0, 1, 2), reverse_complement=True):

    def find_orfs(rnaseq, offset):
        prots = []
        tracking = []

        for i in range(offset, len(rnaseq), 3):
            codon = rnaseq[i:i + 3]
            if len(codon) != 3:
                break

            prot = rna2prot[codon]

            if prot == "M":
                tracking.append((i, []))

            if prot == "Stop":
                prots.extend((idx, "".join(protseq)) for idx, protseq in tracking)
                tracking = []

            for idx, seq in tracking:
                seq.append(prot)

        return prots

    all_prots = []

    if reverse_complement:
        for offset in offsets:
            prots = find_orfs(reverse_comp(rnaseq), offset)
            for prot in prots:
                all_prots.append((f"rev-{offset}",) + prot)

    for offset in offsets:
        prots = find_orfs(rnaseq, offset)
        for prot in prots:
            all_prots.append((f"fwd-{offset}",) + prot)

    return all_prots

def main(fname):
    seqs = read_fasta(fname)

    uniq_prots = set()

    for name, dnaseq in seqs.items():
        prots = find_all_orfs(dna2rna(dnaseq))

        for dircode, ind, prot in prots:
            uniq_prots.add(prot)

    for prot in uniq_prots:
        print(prot)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file"
        )

    args = parser.parse_args()

    main(args.fname)
