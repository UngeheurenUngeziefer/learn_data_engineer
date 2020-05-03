x = int(input())
bfm = bf = 0

while x != 0:
    b = int(input())
    if x == b:
        bf += 1
        if bf > bfm:
            bfm = bf
    else:
        bf = 0
    x = b
print(bfm+1)
