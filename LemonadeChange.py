def lemonadeChange(bills):
    d = dict()
    for bill in bills:
        if bill == 5:
            d[bill] = d.get(bill, 0) + 1
        elif bill == 10:
            if d.get(5,-1) < 1:
                return False
            else:
                d[5] -= 1
                d[10] = d.get(10, 0) + 1
        elif bill == 20:
            if (d.get(5, 0) < 1) or (d.get(10, 0) < 1):
                if d.get(5,0) < 3:
                    return False
                else:
                    d[5] -= 3
                    d[20] = d.get(20, 0) + 1
                    continue
            else:
                d[5] -= 1
                d[10] -= 1
                d[20] = d.get(20, 0) + 1
    return True


print(lemonadeChange([5,5,5,5,20,20,5,5,20,5]))