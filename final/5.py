def plus(a, b):
    return (a[0]*b[1]+a[1]*b[0], a[1]*b[1])
def minus(a, b):
    return plus(a, (-b[0], b[1]))
def times(a, b):
    return (a[0]*b[0], a[1]*b[1])
def div(a, b):
    return times(a, (b[1], b[0]))
def term(n):
    if n == 1:
        return (4, 1)
    elif n == 2:
        return (17, 4)
    else:
        return minus((108, 1), div(minus((815, 1), div((1500, 1), term(n-2))), term(n-1)))
def fracToFloat(n):
    return n[0]/n[1]
def termFloat(n):
    if n == 1:
        return 4.0
    elif n == 2:
        return 4.25
    else:
        return 108 - (815 - 1500/termFloat(n-2))/termFloat(n-1)
mode = input() #параметр, задающий режим работы
n = int(input()) #параметр, задающий количество членов последовательности
if mode == "frac":
    for i in range(1, n+1):
        print(fracToFloat(term(i)), end=" ")
elif mode == "float":
    for i in range(1, n+1):
        print(termFloat(i), end=" ")
# при n=30
# дроби ~26 с
# float ~2.5 с
# для меньших n сравнить время не удалось (слишком быстро)