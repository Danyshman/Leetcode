def addBinary(a,b):
    if len(a) < len(b):
        a = ('0'*(len(b)-len(a))) + a
    if len(a) > len(b):
        b = ('0'*(len(a)-len(b))) + b

    last_num_index_a = len(a)-1
    last_num_index_b = len(b)-1
    vume = 0
    result = ''
    while last_num_index_a >= 0 and last_num_index_b >= 0:
        if (int(a[last_num_index_a]) + int(b[last_num_index_b]) + vume) == 3:
            result = '1' + result
        if (int(a[last_num_index_a]) + int(b[last_num_index_b]) + vume) == 2:
            result = '0' + result
            if vume == 0:
                vume += 1
        if (int(a[last_num_index_a]) + int(b[last_num_index_b]) + vume) < 2:
            result = str(int(a[last_num_index_a]) + int(b[last_num_index_b]) + vume) + result
            if vume > 0:
                vume -= 1
        last_num_index_a -= 1
        last_num_index_b -= 1
    if vume > 0:
        result = '1' + result
    return result


print(addBinary("1111", "1111"))
