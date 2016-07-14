#! python3

import sys

def toCelcius(fahrenheit):
    val = (5 * (float(fahrenheit) - 32)) / 9
    return val

if __name__ == "__main__":
    celcius = toCelcius(sys.argv[1])
    print(celcius)
