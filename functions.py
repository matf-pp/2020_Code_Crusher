def swap(board, r1, c1, r2, c2):
    t = board[r1][c1]
    board[r1][c1] = board[r2][c2]
    board[r2][c2] = t

def vLineAt(board, r, c):
    location = board[r][c]
    if r-2 >= 0 and location == board[r-1][c] and location == board[r-2][c]:
        return True
    if r-1 >= 0 and r+1<len(board) and location == board[r-1][c] and location == board[r+1][c]:
        return True
    if r+2<len(board) and location == board[r+1][c] and location == board[r+2][c]:
        return True
    
    return False

def hLineAt(board, r, c):
    location = board[r][c]
    if c-2 >= 0 and location == board[r][c-1] and location == board[r][c-2]:
        return True
    if c-1 >= 0 and c+1<len(board[r]) and location == board[r][c-1] and location == board[r][c+1]:
        return True
    if c+2<len(board[r]) and location == board[r][c+1] and location == board[r][c+2]:
        return True
    
    return False
