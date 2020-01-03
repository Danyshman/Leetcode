def duplicateZeros(arr):
    temp = arr.copy()
    temp_ind = 0
    i = 0
    while i < len(arr):
        if temp[temp_ind] == 0:
            arr[i] = 0
            if i == len(arr)-1:
                return arr
            arr[i+1] = 0
            i += 2
            temp_ind += 1
        else:
            arr[i] = temp[temp_ind]
            temp_ind += 1
            i += 1
    return arr


print(duplicateZeros([1,0,2,3,0,4,5,0]))


