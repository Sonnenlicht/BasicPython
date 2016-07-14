#! python3

def power_list(numbers):
    newlist = []
    newlist = [numbers[i] ** i for i in range(len(numbers))]
    return newlist

numbers = [78, 700, 82, 16, 2, 3, 9.5]
numlist = power_list(numbers)
print(numlist)

divlist = [integers for integers in range(100, 300) if (integers % 6 == 0) and (integers % 10 == 0)]
print(divlist)

matrix = [[row * 3 + incr for incr in range(1, 4)] for row in range(4)]
newlist = []
def flatten(matrix):
        newlist.append([matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))])
        print(newlist[0])

flatten(matrix)        
    
    
