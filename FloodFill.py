def floodFill(image, sr, sc, newColor):
    r_len = len(image)
    c_len = len(image[0])
    visited = set()
    should_visit = set()
    should_visit.add((sr,sc))
    while len(should_visit) != 0:
        r,c = should_visit.pop()

        if (r,c) not in visited:
            if r + 1 < r_len and image[r + 1][c] == image[r][c]:
                should_visit.add((r + 1, c))
            if r - 1 >= 0 and image[r - 1][c] == image[r][c]:
                should_visit.add((r - 1, c))
            if c + 1 < c_len and image[r][c + 1] == image[r][c]:
                should_visit.add((r, c + 1))
            if c - 1 >= 0 and image[r][c - 1] == image[r][c]:
                should_visit.add((r, c - 1))
            image[r][c] = newColor
            visited.add((r, c))
    return image


print(floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))