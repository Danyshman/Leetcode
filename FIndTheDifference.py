def findTheDifference(s, t):
    s_dict = dict()
    t_dict = dict()
    for letter in s:
        s_dict[letter] = s_dict.get(letter, 0) + 1
    for letter in t:
        t_dict[letter] = t_dict.get(letter, 0) + 1
    for key,value in t_dict.items():
        if value > s_dict.get(key, 0):
            return key


print(findTheDifference("abcd", "abcde"))
