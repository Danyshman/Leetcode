def canPlaceFlowers(flowerbed, n):
    if flowerbed == [0] and n > 1:
        return False
    elif flowerbed == [0] and n <= 1:
        return True
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and i == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            count += 1
        elif flowerbed[i] == 0 and i == len(flowerbed)-1 and flowerbed[i-1] == 0:
            flowerbed[i] = 1
            count += 1
        elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            count += 1
    return count >= n


print(canPlaceFlowers(flowerbed = [0], n = 2))