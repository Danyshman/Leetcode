def maxArea(height):
    max_area = 0
    i = 0
    j = len(height)-1
    while (i < j):
        min_height = min(height[i], height[j])
        max_area = max((max_area, min_height*(j-i)))
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return max_area


print(maxArea([1,8,6,2,5,4,8,3,7]))