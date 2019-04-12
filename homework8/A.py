n, m = map(int, input().split())
a = []
x, y = 0, 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if a[i][j] > a[x][y]:
            x, y = i, j
print(x, y)