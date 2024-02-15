from itertools import product
i = 0
cnt = 0
for x in product('01', repeat=9):
    print(x)
    cnt += x.count('0')
    i += 1
print(cnt, i)