N = int(input())

while int(N) > 86400:
    N -= 86400
else:
    pass

Sec = "%02d" % (N % 60)
Min = "%02d" % ((int(N) % 3600) / int(60))
Hrs = "%01d" % ((int(N) % 86400) / 3600)
print(str(Hrs) + ':' + str(Min) + ':' + str(Sec))
