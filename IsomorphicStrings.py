def wordPattern(s, t):
    str_arr = list(t)
    pattern_arr = list(s)
    if len(pattern_arr) != len(str_arr):
        return False
    pattern_indexes = dict()
    for i in range(len(pattern_arr)):
        pattern_indexes[pattern_arr[i]] = pattern_indexes.get(pattern_arr[i], '') + "{}".format(i)
    str_indexes = dict()
    for i in range(len(str_arr)):
        str_indexes[str_arr[i]] = str_indexes.get(str_arr[i], '') + "{}".format(i)
    if list(str_indexes.values())==list(pattern_indexes.values()):
        return True
    return False

print(wordPattern('paper','title'))