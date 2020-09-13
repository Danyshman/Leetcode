def minFlips(target):
    count = 0
    rest = '0'
    for i in range(len(target)):
        if target[i] != rest:
            count += 1
            rest = '0' if rest == '1' else '1'
    return count

print(minFlips("00000"))