from collections import Counter

def numSplits(s):
    if len(s) == 1:
        return 0
    counter1 = Counter([])
    counter2 = Counter(s)
    count = 0
    for i in range(len(s)):
        counter2[s[i]] -= 1
        counter1[s[i]] = counter1[s[i]] if counter1[s[i]]+1 else 1
        if counter2[s[i]] == 0:
            counter2.pop(s[i])
        if len(counter1) == len(counter2):
            count += 1
    return count

print(numSplits("acbadbaada"))