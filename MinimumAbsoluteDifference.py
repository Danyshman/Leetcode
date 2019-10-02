def minimumAbsoluteDifference(arr):
    arr.sort()
    min_abs_diff = abs(arr[0]-arr[1])
    result = []
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) < min_abs_diff:
            result.clear()
            min_abs_diff = abs(arr[i]-arr[i+1])
            result.append([arr[i],arr[i+1]])
        elif abs(arr[i]-arr[i+1]) == min_abs_diff:
            result.append([arr[i], arr[i + 1]])
    return result


print(minimumAbsoluteDifference([4,2,1,3]))

