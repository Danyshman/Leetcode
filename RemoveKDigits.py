def removeKdigits(num, k) -> str:
    st = []
    for i in range(len(num)):
        while st and num[i] <= st[-1] and k > 0:
            st.pop()
            k -= 1
        st.append(num[i])
        if k == 0:
            return str(int(''.join(st) + num[i+1:]))
    if len(st) == k:
        return '0'
    while k > 0:
        st.pop()
        k -= 1
    return str(int(''.join(st)))

print(removeKdigits(num = "10", k = 1))