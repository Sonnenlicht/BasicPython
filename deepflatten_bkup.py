#! python3

import copy

intlist = []
def deep_flatten(numlist):
    
    for i in numlist:
         if(type(i) == list):
             deep_flatten(i)
         elif(type(i) == tuple):
             deep_flatten(i)
         else:
             intlist.append(i)
    return intlist      

newlist2 = deep_flatten([[1, 2], [3, [4, 5]]])
print(newlist2)
#newlist = deep_flatten([1, 2, 3, 4])
#print(newlist)
