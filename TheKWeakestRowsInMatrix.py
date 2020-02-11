def kWeakestRows(mat, k):
    sum_arr = []
    rows = len(mat)
    for i in range(rows):
        sum_arr.append((i, sum(mat[i])))
    sum_arr = sorted(sum_arr, key=lambda el: (el[1], el[0]))
    return [sum_arr[i][0] for i in range(k)]


print(kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))