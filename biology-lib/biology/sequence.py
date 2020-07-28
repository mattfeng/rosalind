#!/usr/bin/env python

from .constants import rna2prot

def dna2rna(seq):
    translation = str.maketrans("ACGT", "ACGU")

    return seq.translate(translation)


def reverse_comp(seq, rna=True):
    if rna:
        complement = str.maketrans("ACGU", "UGCA")
    else:
        complement = str.maketrans("ACGT", "TGCA")

    return seq[::-1].translate(complement)

def r2p(seq):
    prot = ""
    for i in range(0, len(seq), 3):
        aa = rna2prot[seq[i:i+3]]

        if aa == "Stop":
            break

        prot += aa

    return prot
