#! python3

import random
import sys

def roll(*dice):
    if not dice:
        dice = [6]
    total = 0
    for die in dice:
        total += random.randint(1, die)
    return total

if __name__=="__main__":
    print(roll(*[int(dice) for dice in sys.argv[1:]]))
    #args = sys.argv[:]


