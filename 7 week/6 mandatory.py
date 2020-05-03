students = [{input() for j in range(int(input()))} for i in range(int(input()))]
everyone, someone = set.intersection(*students), set.union(*students)
print(len(everyone), *sorted(everyone), sep='\n')
print(len(someone), *sorted(someone), sep='\n')
