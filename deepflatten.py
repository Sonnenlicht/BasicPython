#! python3

intlist = []
def deep_flatten(numlist):
    for i in numlist:
         if(type(i) == list) or (type(i) == tuple) or (type(i) == set):
             for j in deep_flatten(i):
                 yield j
         #elif(type(i) == tuple):
         #    deep_flatten(i)
         else:
             yield i
    #return intlist      

newlist2 = list(deep_flatten([[1, 2], ['hi', [4, 5]]]))
print(newlist2)
#print(sum(newlist2))
newlist = list(deep_flatten([1, 2, 3, 4]))
print(newlist)
#print(sum(newlist))

def deep_add(numlist):
    addlist = list(deep_flatten(numlist))
    print(sum(addlist))

deep_add([1, 2, 3, 4])
deep_add([(1, 2), [3, {4, 5}]])

nests = [1, 2, [3, 4, [5],['hi']], [6, [[[7, 'hello']]]]]

# Reference from Internet
def flatten(container):
    for i in container:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in flatten(i):
                yield j
        else:
            yield i

print(list(flatten(nests)))
