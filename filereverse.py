#! python3

import sys

srcfile = sys.argv[1]
print(srcfile)
MySFile = open(srcfile)
#print(MyFile.read())
dstfile = sys.argv[2]
print(dstfile)
MyDFile = open(dstfile,'w')

doi = MySFile.read()
charlen = len(doi)

for i in range(len(doi) - 1, -1, -1):
    MyDFile.write(doi[i])
    #print(doi[i])

MySFile.close()
MyDFile.close()
