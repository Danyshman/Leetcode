def solution(numbers, target):
    uniue_numbers = list(set(numbers))
    uniue_numbers.sort()
    num1 = 0
    num2 = 0
    for i in range(len(uniue_numbers)):
        if (uniue_numbers[i]*2) == target and (numbers.count(uniue_numbers[i])) >= 2:
            num1 = uniue_numbers[i]
            num2 = uniue_numbers[i]
            num1_index = numbers.index(num1)
            num2_index = numbers.index(num2)
            return [num1_index + 1, num2_index + 2]
    for i in range(len(uniue_numbers)):
        for j in range(i+1, len(uniue_numbers)):
            if i == j:
                continue
            if (uniue_numbers[i] + uniue_numbers[j]) == target:
                num1 = uniue_numbers[i]
                num2 = uniue_numbers[j]
    num1_index = numbers.index(num1)
    num2_index = numbers.index(num2)
    return [num1_index+1,num2_index+1]

print(solution([-1, 0], -1))
