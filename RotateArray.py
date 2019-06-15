def rotate(nums, k):
    for i in range(k):
        last_num = nums[-1]
        nums[1::] = nums[0:-1]
        nums[0] = last_num
    return nums


print(rotate([1,2,3,4,5,6,7], k = 3))