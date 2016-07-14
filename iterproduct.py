#! python3

def product(*args):
    mult = 1
    for arg in args:
        mult *= arg
    print(mult)

product(10)
product(5, 6, 8)
product(1, 2, 3, 4, 5, 6, 10)

