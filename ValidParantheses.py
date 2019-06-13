def isValid(s):
    if len(s) % 2 != 0:
        return False
    for i in range(int(len(s)/2)):
        s = s.replace('()', '')
        s = s.replace('{}', '')
        s = s.replace('[]', '')
    if s == '':
        return True
    else:
        return False

print(isValid("([]{{}})[{}[[]]]"))