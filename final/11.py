def destroyChain(list):
    for i in range(len(list)):
        k = i
        while k < len(list)-1 and list[k] == list[k+1]:
            k += 1
        if k - i >= 2:
            for j in range(i, k+1):
                list.pop(i)
            return True, k-i+1
    return False, 0
n = int(input())
a = input().split()
count = 0
con = destroyChain(a)
while con[0]:
    count += con[1]
    con = destroyChain(a)
print(count)