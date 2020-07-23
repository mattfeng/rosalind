#!/usr/bin/env python
"""
fibd.py

Now, rabbits only survive for 3 months: 1 month they are born, and then
they reproduce twice. How many rabbit pairs will exist after n months, 
if each month each adult pair of rabbits produces k pairs of rabbits?

Adults
------
R1                 = 0
R2 = R1 + B1       = 1
R3 = R2 + B2       = 1
R4 = R3 + B3 - B1  = 1
R5 = R4 + B4 - B2  = 2

R(n+1) = Previous Rabbits + Previous Bunnies - Old Rabbits

Bunnies
-------
B1                = 1
B2 = R1 * k       = 0
B3 = R2 * k       = 1
B4 = R3 * k       = 1
B5 = R4 * k       = 1

B(n+1) = Previous Generation Adults * k


Actually, the problem states that k is number of months
the rabbit lives for. So the problem is slightly different.
"""

import argparse

def main(num_months, num_survive):
    # use index 0 as a dummy
    adults  = [-1, 0]
    bunnies = [-1, 1]

    for n in range(2, num_months + 1):
        a = adults[n - 1] + bunnies[n - 1]

        # if old rabbits exist
        if n - num_survive >= 1:
            a -= bunnies[n - num_survive]

        b = adults[n - 1]

        adults.append(a)
        bunnies.append(b)

    print(adults[num_months] + bunnies[num_months])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("num_months",
        help="number of months to solve for",
        type=int
        )

    parser.add_argument("num_survive",
        help="number of month each adult rabbit pair lives for",
        type=int
        )

    args = parser.parse_args()

    main(args.num_months, args.num_survive)

