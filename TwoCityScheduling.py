def twoCitySchedCost(costs):
    num_in_a = len(costs)//2
    num_in_b = num_in_a
    for i in range(len(costs)-1, -1, -1):
        for j in range(i):
            if abs(costs[j][0]-costs[j][1]) < abs(costs[j+1][0]-costs[j+1][1]):
                costs[j], costs[j+1] = costs[j+1], costs[j]
    total = 0
    for cost in costs:
        if cost[0] < cost[1] and num_in_a > 0:
            total += cost[0]
            num_in_a -= 1
        elif cost[0] > cost[1] and num_in_b > 0:
            total += cost[1]
            num_in_b -= 1
        elif num_in_a <= 0:
            total += cost[1]
            num_in_b -= 1
        elif num_in_b <= 0:
            total += cost[0]
            num_in_a -= 1
    return total


print(twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))