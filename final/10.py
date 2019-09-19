text = input()
res = ""
i = 0
while i < len(text):
    if text[i].isnumeric():
        if text[i+1].isnumeric():
            res += int(text[i:i+2])*text[i+2]
            i += 3
        else:
            res += int(text[i])*text[i+1]
            i += 2
    else:
        res += text[i]
        i += 1
for k in range(len(res)//40 + int(len(res)%40 != 0)):
    print(res[40*k:40*(k+1)])