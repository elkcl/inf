a = list(map(int, input().split()))
x = int(input())
index = 1
while len(a) != 0:
    if x <= a[0]:
        index += 1
    a = a[1:]
print(index)
