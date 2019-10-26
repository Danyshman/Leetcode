def binaryGap(N):
    bin_str = str(bin(N))[2::]
    start = None
    max_len = 0
    for i in range(len(bin_str)):
        if start is None and bin_str[i] == '1':
            start = i
        elif start is not None and bin_str[i] == '1':
            max_len = max(max_len, i - start)
            start = i
    return max_len


print(binaryGap(8))