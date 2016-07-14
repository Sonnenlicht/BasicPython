#! python3

import sys

def len_or_none(arg):
    try:
        return(len(arg))
    except TypeError:
        return None

print(len_or_none("hello"))
print(len_or_none(4))
print(len_or_none([]))
print(len_or_none(zip([1, 2], [3, 4])))
print(len_or_none(range(10)))

    
