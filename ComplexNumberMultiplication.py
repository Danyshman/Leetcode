def complexNumberMultiply(a, b):
    a_parts = a.split('+')
    b_parts = b.split('+')
    a_parts[1] = a_parts[1].replace('i', "")
    b_parts[1] = b_parts[1].replace('i', '')
    ans1 = str((int(a_parts[0]) * int(b_parts[0])) - (int(a_parts[1]) * int(b_parts[1])))
    ans2 = str((int(a_parts[0]) * int(b_parts[1])) + (int(a_parts[1]) * int(b_parts[0])))
    return str(ans1) + "+" + str(ans2)+'i'



print(complexNumberMultiply("1+-1i", "1+-1i"))