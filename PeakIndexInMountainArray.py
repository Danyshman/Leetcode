def peakIndexMountainArray(A):
    left = 0
    right = len(A) -1
    while left <= right:
        mid = (left+right)//2
        if A[mid-1] < A[mid] > A[mid + 1]:
            return mid
        elif A[mid-1] > A[mid] > A[mid+1]:
            right = mid -1
        else:
            left = mid + 1