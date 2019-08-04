def nextGreaterElement(nums1, nums2):
    answer = []
    for num in nums1:
        if nums2.index(num) == len(nums2)-1:
            answer.append(-1)
            continue
        max_num2 = max(nums2[nums2.index(num) + 1::])
        if num >= max_num2:
            answer.append(-1)
        else:
            for i in range(nums2.index(num)+1, len(nums2)):
                if nums2[i] > num:
                    answer.append(nums2[i])
                    break
    return answer


print(nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))
