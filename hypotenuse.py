#! python3
import sys
import math

def get_hypotenuse(a, b):
    sum = (a*a) + (b*b)
    #hyp = sum ** 0.5
    hyp = math.sqrt(a**2 + b**2)
    return hyp

if __name__ == "__main__":
    result = get_hypotenuse(float(sys.argv[1]), float(sys.argv[2]))
    print('Hypotenuse value: ' + str(result))

    
