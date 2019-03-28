n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[:i] + a[::-1] == (a[:i] + a[::-1])[::-1]:
        print(i)
        print(' '.join(map(str, a[:i][::-1])))
        break
