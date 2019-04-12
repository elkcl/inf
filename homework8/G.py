n = int(input())
a = []
res = True
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    if not res:
        break
    for j in range(n):
        if a[i][j] != a[j][i]:
            res = False
            break
if res:
    print("YES")
else:
    print("NO")