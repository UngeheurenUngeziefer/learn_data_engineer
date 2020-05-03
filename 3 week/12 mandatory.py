A = input()
num = 0
for i in range(len(A)):
    if A[i] == 'f':
        num += 1
        if num == 2:
            print(i)
if num == 1:
    print('-1')
elif 'f' not in A:
    print('-2')
