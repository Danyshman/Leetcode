def printVerically(s):
    arr = s.split(' ')
    max_len = 0
    result = []
    for word in arr:
        if len(word) > max_len:
            max_len = len(word)
    for i in range(len(arr)):
        arr[i] = arr[i] + ' ' * (max_len-len(arr[i]))
    for i in range(max_len):
        temp = ''
        for j in range(len(arr)):
            temp += arr[j][i]
        result.append(temp.strip(' '))
    return result


print(printVerically("CONTEST IS COMING"))
