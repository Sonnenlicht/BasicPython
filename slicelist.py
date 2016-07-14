#! python3

fruits = ["poms", "apples", "pears", "bananas", "mangoes"]

def slice_last3(fruits):
    return fruits[len(fruits)-3:len(fruits)]

last3 = slice_last3(fruits)
print(last3)

#import countword


