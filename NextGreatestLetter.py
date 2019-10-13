def nextGreatestLetter(letters, target):
    int_letters = []
    for letter in letters:
        if ord(letter) > ord(target):
            int_letters.append(ord(letter))
        else:
            int_letters.append(1000)
    return letters[int_letters.index(min(int_letters))]


print(nextGreatestLetter(["c", "f", "j"], 'd'))