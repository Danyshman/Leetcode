def licenseKeyFormatting(S,K):
    S = S.replace('-', '').upper()
    len_s = len(S)
    if len_s <= K:
        return S.upper()
    first_group = len_s%K
    main_group = len_s//K
    ans = ''
    index = 0
    for i in range(first_group):
        ans += S[index]
        index += 1
    for i in range(main_group):
        ans += '-'
        for j in range(K):
            ans += S[index]
            index += 1

    if ans[0] == '-':
        return ans[1:]
    else:
        return ans



print(licenseKeyFormatting("---", 3))
