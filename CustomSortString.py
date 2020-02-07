def customSortString(S, T):
    s_dict = dict()
    for i in range(len(S)):
        s_dict[S[i]] = i
    count_t = [0 for i in range(len(S))]
    count_t.append('')
    for i in range(len(T)):
        if s_dict.get(T[i], False) or s_dict.get(T[i])==0:
            count_t[s_dict.get(T[i])] += 1
        else:
            count_t[-1] += (T[i])
    result = ''
    for i in range(len(count_t)-1):
        result += S[i]*count_t[i]
    result += count_t[-1]
    return result


print(customSortString('cba', 'abcd'))

a = [0 for i in range(5)]