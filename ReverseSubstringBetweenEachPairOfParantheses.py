def reverseParantheses(s):
    paran_index = []
    last_pair_index = None
    for i in range(len(s)):
        if s[i] == '(':
            paran_index.append((i, None))
            last_pair_index = None
        elif s[i] == ")" and last_pair_index is None:
            paran_index[-1] = (paran_index[-1][0], i)
            last_pair_index = -2
        elif s[i] == ')' and last_pair_index:
            if paran_index[last_pair_index][1] is not None:
                last_pair_index -= 1
                while paran_index[last_pair_index][1] is not None:
                    last_pair_index -= 1
                paran_index[last_pair_index] = (paran_index[last_pair_index][0], i)
                last_pair_index -= 1
            else:
                paran_index[last_pair_index] = (paran_index[last_pair_index][0], i)
                last_pair_index -= 1
    for i in range(len(paran_index)-1, -1, -1):
        start = paran_index[i][0]
        end = paran_index[i][1]
        s = s[:start] + s[start:end+1][::-1] + s[end+1::]
    s = s.replace('(', "")
    s= s.replace(')', '')
    return s


print(reverseParantheses("n(ev(t)((()lfevf))yd)cb()"))
