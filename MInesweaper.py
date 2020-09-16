from collections import deque


def updateBoard(board, click):
    if not board:
        return board
    queue = deque([click])
    height = len(board)
    width = len(board[0])
    visited = set((click[0], click[1]))
    while queue:
        r, c = queue.popleft()
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        elif board[r][c] == 'E':
            count_mines = 0
            unrevealed_neighbors = []
            for rr, cc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1], [r+1, c+1], [r-1, c-1], [r+1, c-1], [r-1, c+1]]:
                if 0 <= rr < height and 0 <= cc < width:
                    if board[rr][cc] == 'M':
                        count_mines += 1
                    elif board[rr][cc] == 'E' and (rr, cc) not in visited:
                        unrevealed_neighbors.append([rr, cc])
            if count_mines == 0:
                board[r][c] = 'B'
                queue.extend(unrevealed_neighbors)
                for rr, cc in unrevealed_neighbors:
                    visited.add((rr, cc))
            else:
                print(count_mines)
                board[r][c] = str(count_mines)
    return board

print(updateBoard([ ['E', 'E', 'E', 'E', 'E'],
                    ['E', 'E', 'M', 'E', 'E'],
                    ['E', 'E', 'E', 'E', 'E'],
                    ['E', 'E', 'E', 'E', 'E']],[3,0]))


