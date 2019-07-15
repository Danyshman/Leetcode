def isPalindrome(s):
    s = s.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for letter in s:
        if letter not in alphabet:
            s = s.replace(letter, '')
    if len(s) % 2 == 0:
        return (s[0:int(len(s)/2)]) == (s[int(len(s)/2)::][::-1])
    else:
        return s[0:len(s) // 2] == (s[(len(s) // 2)+1::])[::-1]


print(isPalindrome("race a car"))