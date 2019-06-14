def plusOne(digits):
    number = ''
    for num in digits:
        number += str(num)
    number = int(number)+1
    return_num = []
    for num in str(number):
        return_num.append(int(num))
    return return_num

print(plusOne([9]))