a = int(input())
b = int(input())
c = int(input())
if a == b or b == c or a == c:
    if a == b and b == c and a == c:
        print(3)
    else:
        print(2)
else:
    print(0)
