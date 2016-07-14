#! python3

# List function - Join 2 lists

def combine_lists(first, second):
    #first.append(second) #[1,2,3,[4,5,6]]
    first.extend(second)  #[1,2,3,4,5,6] 
    return first          #first is mutated (first + last)

first=[1,2,3]
second=[4,5,6]
new_lists = []
new_lists = combine_lists(first,second)
print(new_lists)

new_lists.remove(new_lists[0])
print(new_lists)
new_lists.remove(new_lists[-1])
print(new_lists)

names = ['Alice', 'Bob', 'Christy', 'Jules']
names.remove('Bob')
print(names)

words = ['these', 'are', 'some', 'words']
sentence = '\n'.join(words)
print(sentence)
