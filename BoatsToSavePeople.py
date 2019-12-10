def numRescueBoats(people, limit):
    people.sort()
    l, h = 0, len(people) -1
    total_boats = 0
    while l <= h:
        total_boats += 1
        if people[l] + people[h] <= limit:
            l += 1
        h -= 1
    return total_boats


print(numRescueBoats([5,1,4,2], 6))

