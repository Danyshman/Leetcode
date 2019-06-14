def lengthOfLastWord(s):
    list_of_words = s.split()
    if list_of_words == []:
        return 0
    else:
        return len(list_of_words[-1])


print(lengthOfLastWord('     '))