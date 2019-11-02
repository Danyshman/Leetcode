def intervalIntersection(A, B):
    ans = []
    for i in A:
        for j in B:
            if i[0] <= j[0] <= i[1]:
                ans.append([j[0], min(i[1], j[1])])
            elif j[0] <= i[0] <= j[1]:
                ans.append([i[0], min(j[1], i[1])])
    return ans


print(intervalIntersection(A = [[-10,-4],[0,2],[5,10],[13,23],[24,25]], B = [[-8,5],[8,12],[15,24],[25,26]]))