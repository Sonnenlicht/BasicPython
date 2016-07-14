#! python3

def dict_from_truple(truple):
    #for i in truple:
     #   print(i)
    new_dict = {}
    for i in range(len(truple)):
        new_dict.setdefault(truple[i][0],truple[i][1:])
    print(new_dict) 
    

dict_from_truple([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
dict_from_truple([(1, 2, 3, 4), (5, 6, 7, 8)])

