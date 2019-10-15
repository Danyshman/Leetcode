def checkRecord(s):
    a_count = s.count('A')
    is_late = 'LLL' in s
    if a_count > 1 or is_late:
        return False
    else:
        return True


print(checkRecord("PPALLL"))