#!/usr/bin/env python

def read_fasta(f):
    """Read in a FASTA file.

    :param file f: file handler to input file containing fasta string.
    :return: Dictionary containing sequence IDs and sequence values.
    :rtype: dict
    """
    seqs = {}

    header = f.readline().strip().lstrip(">")
    while True:
        seq = ""

        # read in fasta sequence body
        while True:
            nextline = f.readline().strip()

            if len(nextline) == 0 or nextline.startswith(">"):
                seqs[header] = seq

                if len(nextline) == 0:
                    return seqs

                header = nextline.lstrip(">")
                break

            seq += nextline

    return seqs

