n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
i, j = map(int, input().split())
for x in range(n):
    temp = a[x][i]
    a[x][i] = a[x][j]
    a[x][j] = temp
for row in a:
    print(' '.join(list(map(str, row))))