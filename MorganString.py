num_test = input()
A = []
B = []

for i in range(int(num_test)):
    str1 = input()
    A.append(str1)
    str2 = input()
    B.append(str2)
  
for i in range(len(A)):
    C = ''
    A_n = A[i]
    B_n = B[i]
    while A_n != '' or B_n != '':
        if A_n == '':
            C += B_n
            break
        if B_n == '':
            C += A_n
            break
        if A_n[0] > B_n[0]:
            C += B_n[0]
            #print(C)
            B_n = B_n[1:]
        else:
            C += A_n[0]
            #print(C)
            A_n = A_n[1:]
    print(C)
