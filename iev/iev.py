#!/usr/bin/env python

"""
iev.py

Calculating Expected Offspring
==============================
"""

from collections import defaultdict
from itertools import product

import argparse

def cross(g1, g2):
    """Returns the probability of offspring genotypes.

    :param str g1: Genotype 1
    :param str g2: Genotype 2
    :return: Probability matrix of the genotypes of the offspring.
    :rtype: defaultdict(float)
    """

    g1_haploid = product(*g1.split(","))
    g2_haploid = product(*g2.split(","))

    probs = defaultdict(float)

    count = 0
    for h1, h2 in product(g1_haploid, g2_haploid):
        offspring_g = ",".join("".join(sorted(i)) for i in zip(h1, h2))
        count += 1
        probs[offspring_g] += 1.0

    for gtype in probs.keys():
        probs[gtype] /= count

    return probs

def main(parents):
    total_expected_dom = 0
    dom_ptypes = ["AA", "Aa"]

    for parent_gtype, count in parents.items():
        probs = cross(parent_gtype[:2], parent_gtype[2:])

        for ptype in dom_ptypes:
            total_expected_dom += 2 * count * probs[ptype] # 2 children

    print(total_expected_dom)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("AAAA", type=int)
    parser.add_argument("AAAa", type=int)
    parser.add_argument("AAaa", type=int)
    parser.add_argument("AaAa", type=int)
    parser.add_argument("Aaaa", type=int)
    parser.add_argument("aaaa", type=int)

    args = parser.parse_args()

    main({
        "AAAA": args.AAAA,
        "AAAa": args.AAAa,
        "AAaa": args.AAaa,
        "AaAa": args.AaAa,
        "Aaaa": args.Aaaa,
        "aaaa": args.aaaa 
        })
