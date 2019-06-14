def merge(nums1, m, nums2, n):
    nums1[m::] = nums2[0:n]
    temp = 0
    for i in range(len(nums1)-1):
        for j in range(i+1, len(nums1)):
            if nums1[i] > nums1[j]:
                temp = nums1[i]
                nums1[i] = nums1[j]
                nums1[j] = temp
    return nums1




print(merge([1,2,3,0,0,0],3, [2,5,6], 3))