def detectCapital(word):
    is_all_cap = True
    is_all_low = True
    is_first_cap = True
    is_all_low_except_first = True
    for i in range(len(word)):
        if i == 0 and word[i].islower():
            is_first_cap = False
        if i != 0 and word[i].isupper():
            is_all_low_except_first = False
        if word[i].islower():
            is_all_cap = False
        if word[i].isupper():
            is_all_low = False
    return is_all_cap or is_all_low or (is_first_cap and is_all_low_except_first)


print(detectCapital("gAFSDFfsdf"))