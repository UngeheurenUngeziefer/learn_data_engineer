with open('input.txt', 'r') as f:
    nums = f.read().splitlines()
dict = {}

for i in nums:
    cand, vote = i.split()
    dict[cand] = dict.get(cand, 0) + int(vote)

for cand, vote in sorted(dict.items()):
    print(cand, vote)
