#! python3

import sys

op1 = sys.argv[1]
op2 = sys.argv[2]

if(float(op1) > float(op2)):
    diff_val = float(op1) - float(op2)
else:
    diff_val = float(op2) - float(op1)
    
print('Difference between two values: ' + str(diff_val))

