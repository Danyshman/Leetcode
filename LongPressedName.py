def isLongPressed(name, typed):
    i = 0
    j = 0
    while True:
        target = name[i]
        temp1 = 0
        temp2 = 0
        for l in range(i, len(name)):
            if name[l] == target:
                temp1 += 1
                i += 1
            else:
                break
        for k in range(j, len(typed)):
            if typed[k] == target:
                temp2 += 1
                j += 1
            else:
                break
        if temp1 > temp2:
            return False
        if i >= len(name) and j >= len(typed):
            break
    return True

print(isLongPressed(name = "laiden", typed = "laiden"))
