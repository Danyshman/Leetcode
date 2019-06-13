def reverse(x):
    return_num = str(x)[::-1]
    if x<0:
        if ((int(return_num[:-1])*-1) > 2147483647) or ((int(return_num[:-1])*-1) < -2147483647):
            return 0
        else:
            return int(return_num[:-1])*-1
    else:
        if (int(return_num)>2147483647) or (int(return_num)*-1 < -2147483647):
            return 0
        else:
            return int(return_num)

print(reverse(-2147483648))


