def plus(a, b):
    return (a[0]*b[1]+a[1]*b[0], a[1]*b[1])
def shorten(a):
    x = a[0]
    y = a[1]
    while x != 0 and y != 0:
        if abs(x) > abs(y):
            x = x % y
        else:
            y = y % x
    if x != 0:
        res = abs(x)
    else:
        res = abs(y)
    return (a[0] // res, a[1] // res)
a, b = map(int, input().split())
c, d = map(int, input().split())
print(' '.join(map(str, shorten(plus((a, b), (c, d))))))