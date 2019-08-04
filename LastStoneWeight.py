def lastStoneWeight(stones):
    while True:
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
        else:
            y = max(stones)
            temp = stones.copy()
            temp.pop(stones.index(y))
            x = max(temp)
            if x != y:
                stones[stones.index(y)] = y-x
                stones.pop(stones.index(x))
            elif x == y:
                stones.pop(stones.index(x))
                stones.pop(stones.index(y))


print(lastStoneWeight([2,7,4,1,8,1]))
