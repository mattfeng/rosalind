#!/usr/bin/env python
"""
lia.py

Independent Alleles
===================

Let p(k, g) be the probability of one organism having genotype g in the kth generation.
Notice that all the organisms are independent of each other, and so are the traits.

Because of this independence, we only need to look at the probability that any one
offspring has genotype AaBb (and then we can use the binomial theorem to solve for
the desired probability of at least N).

We can further reduce the complexity by using the Law of Independent Assortment, which
states that the probability of having genotype AaBb is equal to P(Aa) * P(Bb). This
means we only need to solve for P(Aa), and then we can square the value to get P(AaBb).
"""

import argparse
import math

from collections import defaultdict

def main(k, N):
    offspring_genotype_probs = {
        "AA": {"AA": 0.50, "Aa": 0.50, "aa": 0.00},
        "Aa": {"AA": 0.25, "Aa": 0.50, "aa": 0.25},
        "aa": {"AA": 0.00, "Aa": 0.50, "aa": 0.50},
        }

    genotype_prob = {
        0: {"AA": 0, "Aa": 1, "aa": 0},
        }

    # Construct the probability distribution of genotypes
    # for the kth generation

    for gen in range(1, k + 1):
        dist = defaultdict(float)

        genotypes = ["AA", "Aa", "aa"]
        for genotype in genotypes:
            dist[genotype] = sum(
                offspring_genotype_probs[g][genotype] * genotype_prob[gen - 1][g]
                for g in genotypes
                )

        s = 0
        for g, p in dist.items():
            s += p
        assert abs(s - 1) < 1e-7, f"bad distribution for generation {gen}: {dist}"

        genotype_prob[gen] = dist

    p_AaBb = genotype_prob[gen]["Aa"] ** 2
    max_N = 2 ** k
    p_less = 0
    for i in range(0, N):
        p_less += math.comb(max_N, i) * (p_AaBb ** i) * ((1 - p_AaBb) ** (max_N - i))

    print(1 - p_less)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("k",
        help="number of generations",
        type=int
        )

    parser.add_argument("N",
        help="value to compute probabilty for",
        type=int
        )

    args = parser.parse_args()

    main(args.k, args.N)


