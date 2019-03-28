a = list(map(int, input().split()))
res = 1000
for i in a:
    if i > 0:
        if i < res:
            res = i
print(res)
