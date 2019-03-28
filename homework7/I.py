a = list(map(int, input().split()))
hasOdd = False
for i in a:
    if i % 2 == 1:
        if not hasOdd:
            res = i
            hasOdd = True
        elif i < res:
            res = i
if hasOdd:
    print(res)
else:
    print(0)
