def divisorGame(N):
    d = dict()
    d[2] = True
    d[3] = False
    for i in range(4, N+1):
        if d[i-1] is False:
            d[i] = True
        else:
            for key, value in list(d.items())[::-1]:
                if i % (i-key) == 0 and value is False:
                    d[i] = True
                    break
            d[i] = d.get(True, False)
    return d[N]


print(divisorGame(1))
