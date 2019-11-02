def spiralMatrixIII(R, C, r0, c0):
    grid = [[i for i in range(C)] for __ in range(R)]
    ans = []
    curr_c_left = c0
    curr_c_right = c0
    curr_c = c0
    curr_r_up = r0
    curr_r_down  = r0
    curr_r = r0
    uniq_vals = dict()
    while len(ans) != R * C:
        #       To right
        while len(grid[0]) > curr_c:
            if curr_c > curr_c_right:
                curr_c_right = curr_c
                break
            if uniq_vals.get((curr_r, curr_c), False) is False:
                ans.append([curr_r, curr_c])
                uniq_vals[(curr_r, curr_c)] = True
            curr_c = curr_c+1
            if curr_c == len(grid[0]):
                curr_c -= 1
                break
        while len(grid) > curr_r:
            if curr_r > curr_r_down:
                curr_r_down = curr_r
                break
            if uniq_vals.get((curr_r, curr_c), False) is False:
                ans.append([curr_r, curr_c])
                uniq_vals[(curr_r, curr_c)] = True
            curr_r = curr_r+1
            if curr_r == len(grid):
                curr_r -= 1
                break
        while curr_c >= 0:
            if curr_c < curr_c_left:
                curr_c_left = curr_c
                break
            if uniq_vals.get((curr_r, curr_c), False) is False:
                ans.append([curr_r, curr_c])
                uniq_vals[(curr_r, curr_c)] = True
            curr_c = curr_c-1
            if curr_c < 0:
                curr_c += 1
                break
        while curr_r >= 0:
            if curr_r < curr_r_up:
                curr_r_up = curr_r
                break
            if uniq_vals.get((curr_r, curr_c), False) is False:
                ans.append([curr_r,curr_c])
                uniq_vals[(curr_r, curr_c)] = True
            curr_r = curr_r-1
            if curr_r < 0:
                curr_r += 1
                break
    return ans


print(spiralMatrixIII(R = 1, C = 4, r0 = 0, c0 = 0))

