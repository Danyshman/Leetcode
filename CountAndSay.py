def countAndSay(n):
    count_and_say_seq = ['1','11','21','1211','111221']
    for j in range(25):
        target = count_and_say_seq[-1]
        indexes = [0]
        for i in range(len(target)-1):
            if target[i] != target[i+1]:
                indexes.append(i+1)
        return_seq = ''
        indexes.append(len(target))
        for i in range(len(indexes)-1):
            return_seq += str(len(target[indexes[i]:indexes[i+1]])) + str(target[indexes[i]])
        count_and_say_seq.append(return_seq)
    return count_and_say_seq[n-1]


print(countAndSay(4))

