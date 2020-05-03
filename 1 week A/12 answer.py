A = int(input())
B = int(input())
N = int(input())

R = ((N * A) + ((N * B) // 100))
C = ((N * B) % 100)
print(str(R) + ' ' + str(C))
