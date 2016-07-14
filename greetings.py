#! python3

import sys
import my_module
import clionly

arguments = sys.argv[1:]
everything = " ".join(arguments)
if __name__ == "__main__":
    if arguments:
        print("Hello {}!".format(everything))
    else:
        print("Hello world!")

my_module
clionly
