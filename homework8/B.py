n = int(input())
a = []
for i in range(n):
    a.append(["."] * n)
for i in range(n):
    for j in range(n):
        if i == j or n-i-1 == j or i == (n-1)/2 or j == (n-1)/2:
            a[i][j] = "*"
for row in a:
    print(' '.join(list(map(str, row))))