#! python3

import sys
import random

srcfile = sys.argv[1]
MySFile = open(srcfile)
dstfile = sys.argv[2]
MyDFile = open(dstfile, 'w')

contentlines = MySFile.read()

contentlist = contentlines.splitlines()
#print(contentlist)
random.shuffle(contentlist)
#print(shufflelist)
print(contentlist)

for i in contentlist:
    MyDFile.write(i)
    MyDFile.write('\n')

MySFile.close()
MyDFile.close()
