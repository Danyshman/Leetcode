def canConstruct(ransomNote, magazine):
    mag_dic = dict()
    for l in magazine:
        mag_dic[l] = mag_dic.get(l, 0) + 1
    for l in ransomNote:
        if (mag_dic.get(l, 0) - 1) < 0:
            return False
        else:
            mag_dic[l] -= 1
    return True


print(canConstruct("a", "b"))
