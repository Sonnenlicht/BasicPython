#! python3

import sys

def dollars(money):
    val = round(float(money)/1, 2)
    dollar_str = '$' + str("%.2f" % val)
    return dollar_str

if __name__ == "__main__":
    money = dollars(sys.argv[1])
    print(money)
