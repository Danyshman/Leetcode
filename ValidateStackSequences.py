def validateStackSequences(pushed, popped):
    temp_arr = []
    pushed_index = 0
    popped_index = 0
    flag = True
    for j in range(len(popped)):
        if len(temp_arr) != 0:
            if temp_arr[-1] == popped[j]:
                temp_arr = temp_arr[:-1]
                popped_index += 1
                continue
        if flag:
            for i in range(pushed_index, len(pushed)):
                if popped[j] == pushed[i]:
                    if i != len(pushed) - 1:
                        pushed_index = i + 1
                        popped_index += 1
                        break
                    else:
                        flag = False
                        popped_index += 1
                        break
                else:
                    temp_arr.append(pushed[i])
        else:
            if temp_arr == popped[popped_index+1:][::-1]:
                return True
            else:
                return False
    if temp_arr == popped[popped_index + 1:][::-1]:
        return True
    else:
        return False



print(validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))