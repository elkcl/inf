flag = [ ["+", "_", "_", "_"], ["|", "n", " ", "/"], ["|", "_", "_", "\\"], ["|", " ", " ", " "] ]
a = []
for i in range(4):
    a.append([0] * 44)
def clearField(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            field[i][j] = " "
def drawFlag(field, num):
    o = (num-1)*5 # сдвиг
    for i in range(4):
        for j in range(4):
            field[i][j+o] = flag[i][j]
    field[1][1+o] = str(num)
def printField(field):
    for row in field:
        print("".join(row))
clearField(a)
for i in range(1, 10):
    drawFlag(a, i)
printField(a)