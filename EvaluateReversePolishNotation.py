import math


def evalRPN(tokens) -> int:
    st = []
    for t in tokens:
        if t[1:].isnumeric() or t.isnumeric():
            st.append(int(t))
        else:
            if t == '*':
                st[-1] = st[-2] * st.pop()
            elif t == '+':
                st[-1] = st[-2] + st.pop()
            elif t == '-':
                st[-1] = st[-2] - st.pop()
            elif t == '/':
                if st[-2] / st[-1] < 0:
                    st[-1] = math.ceil(st[-2] / st.pop())
                else:
                    st[-1] = math.floor(st[-2] / st.pop())

    return st[-1]

print(evalRPN(["2","1","+","3","*"]))