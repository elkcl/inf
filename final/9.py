def nextNum(i, j, n, d): #d -- direction -- текущее направление спирали
    x, y = i, j
    if d % 4 == 0:
        x, y = i-1, j
    elif d % 4 == 1:
        x, y = i, j+1
    elif d % 4 == 2:
        x, y = i+1, j
    elif d % 4 == 3:
        x, y = i, j-1
    if x >= n or y >= n:
        x, y = -1, -1
    return x, y
def to4str(s):
    res = str(s)
    res = ' '*(4-len(res)) + res
    return res
n = int(input())
a = []
for i in range(n):
    a.append([0] * n)
d = 1
i = 0
j = 0
for num in range(1, n**2 + 1):
    a[i][j] = num
    x, y = nextNum(i, j, n, d)
    if x == -1 or a[x][y] != 0:
        d += 1
        x, y = nextNum(i, j, n, d)
    i, j = x, y
for row in a:
    print(''.join(map(to4str, row)))