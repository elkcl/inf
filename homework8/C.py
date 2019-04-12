n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(["*"] * m)
for i in range(n):
    for j in range(m):
        if i % 2 == j % 2:
            a[i][j] = "."
for row in a:
    print(' '.join(list(map(str, row))))