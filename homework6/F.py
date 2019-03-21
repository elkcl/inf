str = input()
firstIndex = str.find('f')
secondIndex = str.find('f', firstIndex + 1)
if firstIndex == -1:
    print(-2)
else:
    print(secondIndex)
