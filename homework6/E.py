str = input()
beginIndex = str.find('f')
endIndex = str.rfind('f')
if beginIndex != -1:
    if beginIndex == endIndex:
        print(beginIndex)
    else:
        print(beginIndex, endIndex)
