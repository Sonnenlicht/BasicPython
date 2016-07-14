#! python3

import sys
import math

def get_cake_and_wine(guests):
    cakes = math.ceil(guests / 8)
    wine_bottles = math.ceil(guests / 3)
    return cakes, wine_bottles

result = get_cake_and_wine(10)
print(result)
