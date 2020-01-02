def pushDominoes(dominoes):
    last_l_ind = None
    last_r_ind = None
    last_let = None
    count_dots = 0
    result = ''
    for i in range(len(dominoes)):
        if dominoes[i] == '.':
            count_dots += 1
        elif dominoes[i] == 'L' and last_r_ind is None and last_let is None:
            result += 'L'*count_dots + 'L'
            count_dots = 0
            last_l_ind = i
            last_let = 'L'
        elif dominoes[i] == 'R' and last_l_ind is None and last_let is None:
            result += '.'*count_dots
            last_r_ind = i
            last_let = 'R'
            count_dots = 0
        elif dominoes[i] == 'L' and last_let == 'R' and count_dots == 0:
            result += 'RL'
            last_let = 'L'
            last_l_ind = i
        elif dominoes[i] == 'L' and last_let == 'R' and count_dots%2==0 and count_dots != 0:
            result += 'R'*(count_dots//2) + 'R' + 'L'*(count_dots//2) + 'L'
            count_dots = 0
            last_let = 'L'
            last_l_ind = i
        elif dominoes[i] == 'L' and last_let == 'R' and count_dots%2==1 and count_dots != 0:
            result += 'R'*(count_dots//2) + "R" + "." +  'L'*(count_dots//2) + 'L'
            count_dots = 0
            last_let = 'L'
            last_l_ind = i
        elif dominoes[i] == 'R' and last_let == 'L':
            result += '.' * count_dots
            count_dots = 0
            last_let = 'R'
            last_r_ind = i
        elif dominoes[i] == 'R' and last_let == 'R':
            result += 'R' + 'R' * count_dots
            count_dots = 0
            last_let = 'R'
            last_r_ind = i
        elif dominoes[i] == 'L' and last_let == 'L':
            result += 'L' * count_dots + 'L'
            count_dots = 0
            last_let = 'L'
            last_r_ind = i
    if last_let=='R':
        result += 'R'*count_dots + 'R'
    else:
        result += '.'*count_dots
    return result


print(pushDominoes("L.....RRRRLLLLLLL.RR"))
