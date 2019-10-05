def reverseString(s):
    if len(s) % 2 == 0:
        begin = 0
        end = len(s)-1
        for i in range(int(len(s)/2)):
            temp = s[begin]
            s[begin] = s[end]
            s[end] = temp
            begin += 1
            end -= 1
    else:
        begin = 0
        end = len(s) -1
        for i in range(int(len(s)//2)):
            temp = s[begin]
            s[begin] = s[end]
            s[end] = temp
            begin += 1
            end -= 1
    return s


print(reverseString(["h","e","l","l","o"]))