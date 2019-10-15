def numEquivDominoPairs(dominoes):
    for i in range(len(dominoes)):
        dominoes[i] = str(dominoes[i][0]) + str(dominoes[i][1])
    d = dict()
    for dominoe in dominoes:
        temp1 = d.get(dominoe, 0)
        temp2 = d.get(dominoe[::-1],0)
        if temp1:
            d[dominoe] = d.get(dominoe) + 1
        elif temp2:
            d[dominoe[::-1]] = d.get(dominoe[::-1]) + 1
        else:
            d[dominoe] = 1
    sum = 0
    for value in d.values():
        sum += int(value*(value-1)/2)
    return sum


print(numEquivDominoPairs([[2,1],[5,4],[3,7],[6,2],[4,4],[1,8],[9,6],[5,3],[7,4],[1,9],[1,1],[6,6],[9,6],[1,3],[9,7],[4,7],[5,1],[6,5],[1,6],[6,1],[1,8],[7,2],[2,4],[1,6],[3,1],[3,9],[3,7],[9,1],[1,9],[8,9]]))
