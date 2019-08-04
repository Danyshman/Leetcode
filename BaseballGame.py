def calPoints(ops):
    first_valid = 0
    second_valid = 0
    sum = 0
    index = 0
    while True:
        if index >= len(ops):
            break
        if ops[index] == 'C':
            ops.pop(index)
            ops.pop(index-1)
            index -= 1
            continue
        index += 1
    for op in ops:
        if op == "+":
            temp = first_valid + second_valid
            sum += first_valid + second_valid
            temp_valid = int(second_valid)
            second_valid = int(first_valid)
            first_valid = temp
        elif op == 'D':
            sum += 2*first_valid
            temp_valid = int(second_valid)
            second_valid = int(first_valid)
            first_valid = 2*first_valid
        else:
            sum += int(op)
            temp_valid = int(second_valid)
            second_valid = int(first_valid)
            first_valid = int(op)
    return sum


print(calPoints(["36","28","70","65","C","+","33","-46","84","C"]))