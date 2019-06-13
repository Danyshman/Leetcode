def romanToInt(s):
    int_num = 0
    IV = s.count('IV')
    IX = s.count('IX')
    XL = s.count('XL')
    XC = s.count('XC')
    CD = s.count('CD')
    CM = s.count('CM')
    int_num += IV * 4
    int_num += IX * 9
    int_num += XL * 40
    int_num += XC * 90
    int_num += CD * 400
    int_num += CM * 900
    s = s.replace('IV', '', IV)
    s = s.replace('IX', '', IX)
    s = s.replace('XL', '', XL)
    s = s.replace('XC', '', XC)
    s = s.replace('CD', '', CD)
    s = s.replace('CM', '', CM)
    for num in s:
        if num == 'M':
            int_num += 1000
        if num == 'D':
            int_num += 500
        if num == 'C':
            int_num += 100
        if num == 'L':
            int_num += 50
        if num == 'X':
            int_num += 10
        if num == 'V':
            int_num += 5
        if num == 'I':
            int_num += 1
    return int_num

print(romanToInt('III'))
