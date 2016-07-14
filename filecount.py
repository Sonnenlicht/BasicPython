#! python3

#program to count the number of occurences of 'people' in a large string

import sys

filename = sys.argv[1]
print(filename)
MyFile = open(filename)
#print(MyFile.read())

doi = MyFile.read()
count = doi.count('i')
print('''Number of occurences of char 'i': ''' + str(count))

inv_doi = doi.title()
inv_doi = inv_doi.swapcase()     

import re
    
word_count = len(re.findall(r'\w+', doi))
print ('Words: ' + str(word_count))

line_count = len(re.findall(r'\n', doi)) + 1
print ('Lines: ' + str(line_count))

print ('Characters: ' + str(len(doi)))

linelist = doi.split('\n')
print(linelist)

line_length = 0
for i in range(len(linelist)):
    if (len(linelist[i]) > line_length):
        line_length = len(linelist[i])

print ('Longest line: ' + str(line_length))
    
    
print(inv_doi)
MyFile.close()
        


