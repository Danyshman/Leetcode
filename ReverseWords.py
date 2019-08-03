def reverseWords(s):
    array_of_words = s.split(" ")
    for i in range(len(array_of_words)):
        array_of_words[i] = array_of_words[i][::-1]
    return " ".join(array_of_words)


print(reverseWords("Let's take LeetCode contest"))