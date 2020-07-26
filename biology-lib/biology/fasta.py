#!/usr/bin/env python
def read_fasta(fname):
    seqs = {}

    with open(fname) as f:
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




