def escapeGhosts(ghosts, target):
    my_min_steps = abs(target[0] - 0) + abs(target[1] - 0)
    ghosts_min_steps = 100000
    for ghost in ghosts:
        ghosts_min_steps = min(ghosts_min_steps, abs(target[0]-ghost[0]) + abs(ghost[1]-target[1]))
    if ghosts_min_steps <= my_min_steps:
        return False
    else:
        return True

print(escapeGhosts(ghosts = [[2, 0]],target = [1, 0]))
