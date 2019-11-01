def firstBadVersion(n):
    start = 1
    end = n
    while start <= end:
        med = (start+end)//2
        temp = isBadVersion(med)
        if start == end and temp:
            return med
        elif temp is False:
            start = med + 1
        elif temp:
            end = med-1


print(firstBadVersion())