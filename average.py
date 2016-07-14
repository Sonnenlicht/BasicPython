#! python3

import sys

arguments = sys.argv[1:]

sum_var = 0
j = 0

try:
    for i in range(len(arguments)):
        sum_var += int(arguments[i])
        j += 1
except ValueError:
    print("Invalid values entered, only numbers allowed!")
    exit(1)

try:
    average = sum_var / j
except ZeroDivisionError:
    print("No numbers in average")
    exit(1)
    
print('Average: ' + str(average))
