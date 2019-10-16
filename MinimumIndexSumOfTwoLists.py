def findRestaurant(list1, list2):
    ans = []
    temp = 10000000
    for i in range(len(list1)):
        if list1[i] in list2 and (i + list2.index(list1[i])) < temp:
            ans = []
            ans.append(list1[i])
            temp = i + list2.index(list1[i])
        elif list1[i] in list2 and (i + list2.index(list1[i])) == temp:
            ans.append(list1[i])
    return ans


print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Burger King","Tapioca Express","Shogun"]))