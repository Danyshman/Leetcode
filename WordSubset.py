def wordSubsets(A, B):
    result = []
    b_word_dict = {}
    for b_word in B:
        for letter in b_word:
            count = b_word.count(letter)
            if b_word_dict.get(letter,0) < count:
                b_word_dict[letter] = count
    for a_word in A:
        flag = True
        for key, value in b_word_dict.items():
            if a_word.count(key) < value:
                flag = False
                break
        if flag:
            result.append(a_word)
    return result


print(wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]))