def countBits(num):
    if num == 0:
        return [0]
    if num == 1:
        return [0,1]
    elif num == 2:
        return [0,1,1]
    elif num == 3:
        return [0,1,1,2]
    else:
        i = 4
        ans = [0,1,1,2]
        base = [2]
        while i <= num:
            new_base = []
            if i <= num:
                ans.append(1)
                i += 1
            for b in base:
                if i <= num:
                    ans.append(b)
                    new_base.append(b)
                    i += 1
                else:
                    return ans
            if i <= num:
                ans.append(2)
                new_base.append(2)
                i += 1
            for b in base:
                if i <= num:
                    ans.append(b+1)
                    new_base.append(b+1)
                    i += 1
                else:
                    return ans
            base = new_base.copy()
        return ans

print(countBits(127))
