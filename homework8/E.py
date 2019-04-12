n = int(input())
a = []
for i in range(n):
    a.append([2] * n)
for i in range(n):
    for j in range(0, n-i-1):
        a[i][j] = 0
    a[i][n-i-1] = 1
for row in a:
    print(' '.join(list(map(str, row))))