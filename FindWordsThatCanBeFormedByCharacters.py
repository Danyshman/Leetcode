def countCharacters(words, chars):
    chars_dic = dict()
    for char in chars:
        chars_dic[char] = chars_dic.get(char, 0) + 1
    result = 0
    for word in words:
        temp_chars = chars_dic.copy()
        is_formed = True
        for let in word:
            if temp_chars.get(let,False) > 0:
                temp_chars[let] = temp_chars.get(let)-1
            else:
                is_formed = False
                break
        if is_formed:
            result += len(word)
    return result


print(countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))