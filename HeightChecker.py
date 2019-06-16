def heightChecker(heights):
    sorted_heights = (heights.copy())
    sorted_heights.sort()
    count = 0
    print(sorted_heights)
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            count += 1
    return count


print(heightChecker([1,1,4,2,1,3]))