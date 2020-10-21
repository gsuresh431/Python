from itertools import combinations

x = '12345'
res = []

# print(list(combinations(x, 2)))
res.extend(list(map(lambda x: str(x[0]) + str(x[1]), list(itertools.combinations(x, 2)))))
res.extend(list(map(lambda x: str(x[0]), list(combinations(x, 1)))))
filter()
print(res)