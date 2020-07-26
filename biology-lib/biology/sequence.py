#!/usr/bin/env python

def dna2rna(seq):
    translation = str.maketrans("ACGT", "ACGU")

    return seq.translate(translation)


def reverse_comp(seq, rna=True):
    if rna:
        complement = str.maketrans("ACGU", "UGCA")
    else:
        complement = str.maketrans("ACGT", "TGCA")

    return seq[::-1].translate(complement)
