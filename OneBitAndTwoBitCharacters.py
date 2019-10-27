def isOneBitCharacter(bits):
    i = 0
    while i < len(bits):
        if bits[i] == 0 and i == len(bits)-1:
            return True
        elif bits[i] == 1:
            i += 2
        elif bits[i] == 0:
            i += 1
    return False


print(isOneBitCharacter([1, 1, 1, 0]))
