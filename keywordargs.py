#! python3

import sys

def print_name(first, last):
    print('My name is ' + first + ' ' + last)
            
if __name__ == "__main__":
    print_name(first="Trey", last="Hunner")
    print_name(last="Hunner", first="Trey")

