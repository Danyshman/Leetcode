def findMedianSortedArrays(nums1, nums2):
    merged = nums1 + nums2
    merged.sort()
    if len(merged)%2==0:
        return (merged[len(merged)//2] + merged[(len(merged)//2)-1]) / 2
    else:
        return merged[len(merged)//2]


print(findMedianSortedArrays(nums1 = [1, 3], nums2 = [2]))