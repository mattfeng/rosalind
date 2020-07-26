#!/usr/bin/env python

"""
mprt.py

Finding a protein motif
=======================

"""

from biology.fasta import read_fasta

import requests
import re
import io
import argparse

def get_protein_fasta(uniprot_id):
    BASE_URL = "https://www.uniprot.org/uniprot/"
    resp = requests.get(BASE_URL + f"{uniprot_id}.fasta")

    fasta = resp.text
    return fasta

def main(fname):
    with open(fname) as f:
        for line in f:
            line = line.strip()
            fasta = get_protein_fasta(line)
            parsed = read_fasta(io.StringIO(fasta))

            for seqid, aaseq in parsed.items():
                matches = re.finditer(r"(?=N[^P][ST][^P])", aaseq)
                out = " ".join(map(str, [match.start() + 1 for match in matches]))
                if len(out) != 0:
                    print(line)
                    print(out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file",
        )

    args = parser.parse_args()

    main(args.fname)
