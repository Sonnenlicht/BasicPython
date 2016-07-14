#! python3

import sys

def isLeapyear(year):
    if(year % 4) == 0:
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
        
if __name__ == "__main__":
    isleap = isLeapyear(int(sys.argv[1]))
    print(isleap)
