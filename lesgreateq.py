#! python3

# Less, Greater, Equal Code

print('Pick your favorite number from 0 to 100: ')
sister_age = int(input())
print('Pick your second favorite number in that range: ')
brother_age = int(input())

if sister_age > brother_age:
    print('Sister is older')
elif sister_age < brother_age:
    print('Brother is older')
else:
    print('Sister and brother are twins')


