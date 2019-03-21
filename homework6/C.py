str = input()
index = len(str)
if index % 2 == 0:
    i = index // 2
else:
    i = index // 2 + 1
print(str[i:], str[:i], sep='')
