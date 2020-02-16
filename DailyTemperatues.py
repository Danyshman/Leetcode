def dailyTemperatures(T):
    st = []
    ans = [0] * len(T)
    for i in range(len(T)):
        while st and T[st[-1]] < T[i]:
            ans[st.pop()] = i - st[-1]
        st.append(i)
    return ans


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))