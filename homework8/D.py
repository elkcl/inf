n = int(input())
a = []
b = []
for i in range(n):
    b.append(i)
b = b[:0:-1] + b
for i in range(n):
    a.append(b[n-i-1:2*n-i-1])
for row in a:
    print(' '.join(list(map(str, row))))