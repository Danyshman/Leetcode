def compress(chars):
    count_val = dict()
    for i in range(len(chars)):
        count_val[chars[i]] = count_val.get(chars[i], 0) + 1
    start = 0
    for key, value in count_val.items():
        if value == 1:
            start += 1
        else:
            chars = chars[:start] + [key] + list(str(value)) + chars[start + value::]
            start += value
    return chars


print(compress(["a","a","b","b","c","c","c"]))
