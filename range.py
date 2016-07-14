#! python3

# Range exercises

def ith_item_power(numlist, index):
    return numlist[index] ** index

a = ith_item_power([3, 2, 5], 2)
print(a)
b = ith_item_power([5, 6, 2, 7, 3], 4)
print(b)    

def power_list(numlist):
    newlist = []
    for i in range(len(numlist)):
        newlist.append(float(numlist[i]) ** i)
    return newlist

numbers = power_list([3,2,5])
print(numbers)
numbers = [78, 700, 82, 16, 2, 3, 9.5]
numbers = power_list(numbers)
print(numbers)

div_list = []
for k in range(100,300, 1):
    if(k%6 == 0):
        if(k%10 == 0):
            div_list.append(k)

print(div_list)
