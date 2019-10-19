def gcdOfStrings(str1, str2):
    if str1[0] != str2[0] or ():
        return ''
    else:
        if len(str1) <= len(str2):
            common_div = str1
            for i in str1:
                if len(str2) % len(common_div) == 0:
                    if common_div * (len(str2) // len(common_div)) == str2 and (common_div * (len(str1) // len(common_div)) == str1):
                        return common_div
                common_div = common_div[:-1]
        else:
            common_div = str2
            for i in str2:
                if len(str1) % len(common_div) == 0:
                    if (common_div * (len(str1) // len(common_div)) == str1) and (common_div * (len(str2) // len(common_div)) == str2):
                        return common_div
                common_div = common_div[:-1]
        return ''



print(gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX","TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))