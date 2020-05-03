days_in_year, num_of_parties = map(int, input().split())
week1 = list(range(6, days_in_year + 1, 7))
week2 = list(range(7, days_in_year + 1, 7))
weekends = sorted(week1 + week2)
a = set()
counter = 0
for i in range(0, num_of_parties + 1):
    f_day, f_step = map(int, input().split())
    strike1 = set(range(f_day, days_in_year + 1, f_step))
    strike2 = strike1 - set(weekends)
    a |= strike2
    counter += 1
    if counter == num_of_parties:
        break
print(len(a))
