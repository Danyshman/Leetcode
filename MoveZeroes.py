def moveZeroes(nums):
    num_of_zeroes = 0
    while True:
        try:
            index = nums.index(0)
            nums.pop(index)
            num_of_zeroes += 1
        except Exception:
            break
    for i in range(num_of_zeroes):
        nums.append(0)
    return nums


print(moveZeroes([0,1,0,3,12]))