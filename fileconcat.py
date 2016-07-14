#! python3

import sys

filenames = list(sys.argv[1:])

for i in filenames:
    try:
        myfile = open(i)
        print('This is ' + i)
    except FileNotFoundError:
        print('No such file or directory: i', file=sys.stderr)
        

    
