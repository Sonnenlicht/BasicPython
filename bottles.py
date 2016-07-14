#! python3

for i in range(100, 1, -1):
    print(str(i) + ' bottles of milk on the wall, ' + str(i) + ' bottles of milk.\n' +
'Take one down, pass it around, ' + str(i-1) + ' bottles of milk on the wall...')
print('''1 bottle of milk on the wall, 1 bottle of milk.
Take one down, pass it around, no more bottles of milk on the wall...
No more bottles of milk on the wall, no more bottles of milk.
Go to the store and buy some more, 99 bottles of milk on the wall...''')
