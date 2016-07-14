#! python3

def vowel_names(names):
    new_names = []
    for i in names:
        if(i.startswith('A') |
           i.startswith('E') |
           i.startswith('I') |
           i.startswith('O') |
           i.startswith('U')):
            new_names.append(i)

    #Working List Comprehension
    #new_names = [i for i in names if(i.startswith('A') | i.startswith('E') | i.startswith('I') | i.startswith('O') | i.startswith('U'))]

    return new_names

names = ["Alice", "Bob", "Christy", "Jules"]
new_names = vowel_names(names)
print(new_names)
names = ["Scott", "Arthur", "Jan", "Elizabeth"]
new_names = vowel_names(names)
print(new_names)
