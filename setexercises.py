#! python3

restaurants_trey = {'Habaneros', 'Karl Strauss', 'Opera', 'Punjabi Tandoor'}
restaurants_diane = {'Siam Nara', 'Punjabi Tandoor', 'Opera'}
restaurants_peter = {'Karl Strauss', 'Opera', 'Habaneros'}

treyNdiane = restaurants_trey.intersection(restaurants_diane)
restaurant_eat = treyNdiane.intersection(restaurants_peter)

print(restaurant_eat)

treyUdiane = restaurants_trey.union(restaurants_diane)
listofkeys = treyUdiane.union(restaurants_peter)

#print(listofkeys)

newdict = dict.fromkeys(listofkeys, 0)
#print(newdict)

for k in newdict.keys():
   if k in restaurants_trey:
       newdict[k] += 1
   if k in restaurants_diane:
       newdict[k] += 1 
   if k in restaurants_peter:
       newdict[k] += 1

print(newdict)


def most_common(setlist):
    keyset = set()
    for i in setlist:
        keyset = keyset.union(i)
   # print(keyset)
    setdict = dict.fromkeys(keyset, 0)

    maxi = 0
    for k in setdict.keys():
        for i in setlist:
            if k in i:
                setdict[k] += 1
        
        maxi = max(maxi, setdict[k])

    resultset = set()
    for k in setdict.keys():
        if(setdict[k] == maxi):
            resultset.add(k) # = resultset + k
            
    #print(maxi)
    #print(setdict)
    print(resultset)
    
myset = [{1, 2}, {2, 3}, {3, 4}]
most_common(myset)
most_common([restaurants_trey, restaurants_diane, restaurants_peter])    

def isunique(strlist):
    strset = set(strlist)
    elements = strset.union(strset)
    #print(strset)
    if len(strlist) - len(strset):
        print('Not Unique')
    else:
        print('Unique')
    
        

numbers1 = [1, 2, 4, 2]
numbers2 = [1, 2, 3, 4]
isunique(numbers1)
isunique(numbers2)
