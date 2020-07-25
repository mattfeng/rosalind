#!/usr/bin/env python

import argparse

def main(fname):
    gc_content = []

    with open(fname) as f:
        label = f.readline().strip().lstrip(">")
        while True:
            seq = ""
            l = ""
            while True:
                l = f.readline().strip()

                # read until EOF or the next FASTA string
                if l.startswith(">") or len(l) == 0:
                    break

                seq += l

            print(label)
            print(seq)

            content = (seq.count("C") + seq.count("G")) / len(seq)
            gc_content.append((label, content))

            # if next is FASTA, keep going, otherwise break out of loop
            if l.startswith(">"):
                label = l.strip().lstrip(">")
            else:
                break

    gc_content_sorted = sorted(gc_content, key=lambda x: x[1], reverse=True)
    max_label, max_pct = gc_content_sorted[0]

    print(gc_content_sorted)

    print(f"{max_label}")
    print(f"{max_pct * 100}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("fname",
        help="path to input file"
        )

    args = parser.parse_args()
    main(args.fname)

