H = int(input())  # length  100
A = int(input())  # +       99
B = int(input())  # -       98
S = A - B
X = (((H - A) + S - 1) // S) + 1
print(X)
