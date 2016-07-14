#! python3

new_dict = {}
def flip_dict(dict):
    for k, v in dict.items():
        new_dict[v] = k
    print(new_dict)

#Dictionary Comprehension for the loop above
    #new_dict = {v:k for k, v in dict.items()}
    #print(new_dict)

mydict = {'a':1,'b':2,'c':3}
flip_dict(mydict)
flip_dict({'Python': "2015-09-15", 'Java': "2015-09-14", 'C': "2015-09-13"})
        
