def intersect(nums1, nums2):
    visited = set()
    ans = set()
    if len(nums1) < len(nums2):
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and j not in visited:
                    ans.add(nums2[j])
                    visited.add(j)
                    break
    else:
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums2[i] == nums1[j] and j not in visited:
                    ans.add(nums1[j])
                    visited.add(j)
                    break
    return ans


print(intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))

