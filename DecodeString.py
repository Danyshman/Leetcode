import re


def decodeString(s):
    while True:
        temp = re.search("\d+\[([a-zA-Z]+)\]", s)
        if temp is None:
            break
        start = temp.start()
        end = temp.end()
        temp = temp.group()
        temp_list = temp.split('[')
        temp_list[-1] = temp_list[-1][:-1]
        s = s[:start] + int(temp_list[0]) * temp_list[1] + s[end:]
    return s


print(decodeString("3[a]2[b4[F]c]"))