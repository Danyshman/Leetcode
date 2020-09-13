def swap(arr, start, end):
    while (start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def pancakeSort(arr):
    arr_sorted = sorted(arr)
    ans = []
    for i in range(len(arr)-1, -1, -1):
        b_idx = arr[:i+1].index(arr_sorted[i])
        arr = swap(arr, 0, b_idx)
        arr = swap(arr, 0, i)
        if b_idx != i:
            if b_idx != 0:
                ans.append(b_idx+1)
            ans.append(i+1)
    return ans

print(pancakeSort([1,2,3]))