def originalDigits(s):
    result = ''
    cld = dict()
    for letter in 'onetwhrzfuivsxg':
        cld[letter] = s.count(letter)
    for i in range(10):
        if i == 0:
            min_letter = cld['z']
            result += '0' * min_letter
            cld['z'] -= min_letter
            cld['e'] -= min_letter
            cld['r'] -= min_letter
            cld['o'] -= min_letter
        elif i == 1:
            min_letter = cld['o'] - cld['u'] - cld['w']
            result += '1' * min_letter
            cld['o'] -= min_letter
            cld['n'] -= min_letter
            cld['e'] -= min_letter
        elif i == 2:
            min_letter = cld['w']
            result += '2' * min_letter
            cld['t'] -= min_letter
            cld['w'] -= min_letter
            cld['o'] -= min_letter
        elif i == 3:
            min_letter = cld['h'] - cld['g']
            result += '3' * min_letter
            cld['t'] -= min_letter
            cld['h'] -= min_letter
            cld['r'] -= min_letter
            cld['e'] -= min_letter
            cld['e'] -= min_letter
        elif i == 4:
            min_letter = cld['u']
            result += '4' * min_letter
            cld['f'] -= min_letter
            cld['o'] -= min_letter
            cld['u'] -= min_letter
            cld['r'] -= min_letter
        elif i == 5:
            min_letter = cld['f']
            result += '5' * min_letter
            cld['f'] -= min_letter
            cld['i'] -= min_letter
            cld['v'] -= min_letter
            cld['e'] -= min_letter
        elif i == 6:
            min_letter = cld['x']
            result += '6' * min_letter
            cld['s'] -= min_letter
            cld['i'] -= min_letter
            cld['x'] -= min_letter
        elif i == 7:
            min_letter = cld['s']
            result += '7' * min_letter
            cld['s'] -= min_letter
            cld['e'] -= min_letter
            cld['v'] -= min_letter
            cld['e'] -= min_letter
            cld['n'] -= min_letter
        elif i == 8:
            min_letter = cld['g']
            result += '8' * min_letter
            cld['e'] -= min_letter
            cld['i'] -= min_letter
            cld['g'] -= min_letter
            cld['h'] -= min_letter
            cld['t'] -= min_letter
        elif i == 9:
            min_letter = cld['i']
            result += '9' * min_letter
            cld['n'] -= min_letter
            cld['i'] -= min_letter
            cld['n'] -= min_letter
            cld['e'] -= min_letter
    return result

print(originalDigits("zeroonetwothreefourfivesixseveneightnine"))
