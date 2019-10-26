def distributeCandies(candies, num_people):
    ans = [0 for __ in range(num_people)]
    i = 0
    candy = 1
    while candies > 0:
        if candies <= candy:
            ans[i] += candies
            candies = 0
        else:
            ans[i] += candy
            candies -= candy
            candy += 1
            if i == len(ans) -1:
                i = 0
            else:
                i += 1
    return ans


print(distributeCandies(candies = 10, num_people = 3))
