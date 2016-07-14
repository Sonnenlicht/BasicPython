#!python3

def get_oldest(date1, date2):
    m1, d1, y1 = date1.split('/')
    m2, d2, y2 = date2.split('/')

    if((y1, m1, d1) > (y2, m2, d2)):
        return date2
    else:
        return date1

old_date = get_oldest("01/27/1832", "01/27/1756")
print(old_date)
old_date = get_oldest("02/29/1972", "12/21/1946")
print(old_date)
old_date = get_oldest("03/24/1946", "02/21/1946")
print(old_date)
old_date = get_oldest("02/20/1946", "02/21/1946")
print(old_date)
old_date = get_oldest("02/19/1946", "02/21/1946")
print(old_date)

def name_key(name):
    return (name[1], name[0])

suzanne = ("Suzanne", "Smith")
michael = ("Michael", "Gambino")

MyName = name_key(michael)
print(MyName)
MyName = name_key(suzanne)
print(MyName)

evelyn = ("Evelyn", "Moore")
jill = ("Jill", "Moore")
tanya = ("Tanya", "Jackson")
ben = ("Ben", "Speigel") 
names = [tanya, evelyn, jill, ben]

from operator import itemgetter
def sort_names(name_list):
    return sorted(name_list, key=itemgetter(1))

sorted_names = (sort_names(names))
print(sorted_names)
    
