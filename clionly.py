#! python3

# Command line only

import sys
if __name__ == "__main__":
    print('Hello world!')
else:
    #print('This module can only be run from the command-line')
    raise ImportError("This module can only be run from the command-line")

