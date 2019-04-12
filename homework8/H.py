n = int(input())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
if k >=0:
    for x in range(n-k):
        b.append(a[k+x][x])
else:
    for x in range(n+k):
        b.append(a[x][-k+x])
print(' '.join(list(map(str, b))))