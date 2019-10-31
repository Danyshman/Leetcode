def maxDistToClosest(seats):
    ones_dict = dict()
    for i in range(len(seats)):
        if seats[i] == 1:
            ones_dict[i] = 1
    if len(list(ones_dict)) == 1:
        for key, item in ones_dict.items():
            return max(abs(len(seats)-1 - int(key)), abs(int(key) - 0))
    else:
        ones_dict = list(ones_dict.items())
        max_len = max(abs(int(ones_dict[0][0]) - 0), abs(len(seats)-1 - int(ones_dict[-1][0])))
        for i in range(1, len(ones_dict)):
            if abs(int(ones_dict[i][0]) - int(ones_dict[i-1][0]))//2 > max_len:
                max_len = abs(int(ones_dict[i][0]) - int(ones_dict[i-1][0]))//2
    return max_len


print(maxDistToClosest([0,1,1,0,0,0]))