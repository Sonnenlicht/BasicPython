#! python3

import sys

filename = sys.argv[1]
print(filename)
MyFile = open(filename)
#print(MyFile.read())

doi = MyFile.read()
nameslist = doi.split('\n')
nameslist = (sorted(nameslist))

MyFile = open(filename,'w')

for i in nameslist:
    MyFile.write(str(i) + '\n')
    #MyFile.write('\n')
