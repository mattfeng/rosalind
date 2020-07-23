"""
iprb.py

Finding the probability of recessive for a Mendelian
trait.

"""

import argparse
import itertools
import functools

def main(k, m, n):
    """
    k homozygous dominant.
    m heterozygous.
    n homozygous recessive.
    """

    total = k + m + n

    prob_table = {
        ("AA", "AA"): k * (k - 1),
        ("AA", "Aa"): k * m,
        ("AA", "aa"): k * n,
        ("Aa", "AA"): m * k,
        ("Aa", "Aa"): m * (m - 1),
        ("Aa", "aa"): m * n,
        ("aa", "AA"): n * k,
        ("aa", "Aa"): n * m,
        ("aa", "aa"): n * (n - 1),
    }
    
    dom_table = {
        ("AA", "AA"): 1.0,
        ("AA", "Aa"): 1.0,
        ("AA", "aa"): 1.0,
        ("Aa", "AA"): 1.0,
        ("Aa", "Aa"): 0.75,
        ("Aa", "aa"): 0.5,
        ("aa", "AA"): 1.0,
        ("aa", "Aa"): 0.5,
        ("aa", "aa"): 0.0
    }
    
    p_dominant = 0
    for comb, p_comb in prob_table.items():
        p_comb /= total * (total - 1)
        p_dominant += p_comb * dom_table[comb]

    print(p_dominant)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("k",
        help="number of homozygous dominant",
        type=int,
        )
    parser.add_argument("m",
        help="number of heterozygous",
        type=int,
        )
    parser.add_argument("n",
        help="number of homozygous recessive",
        type=int,
        )

    args = parser.parse_args()

    main(args.k, args.m, args.n)
