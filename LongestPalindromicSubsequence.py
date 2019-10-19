def longestPalindrome(s):
    old_l = [[0,len(s)]]
    for j in range(len(s)):
        new_path = set()
        for i in old_l:
            if s[i[0]:i[1]] == s[i[0]:i[1]][::-1]:
                return s[i[0]:i[1]]
            new_path.add((i[0], i[1]-1))
            new_path.add((i[0]+1, i[1]))
        old_l = new_path

print(longestPalindrome('ABCDEFK'))


