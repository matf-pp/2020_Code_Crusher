import random

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
def createBoard(numberOfRows,numberOfColumns,numberOfUniquePieces):
    board=[]
    
    for r in range(numberOfRows):
        board.append([])
        for c in range(numberOfColumns):
            board[r].append(random.randint(0,numberOfUniquePieces))
    
    return board

tabela=createBoard(5,5,5)

for elenenti in tabela:
    for element in elenenti:
        print(element)
    print("\n")

def clearSymbols(board,symbol):
    for r in range(len(board)):
        for c in range (len(board[0])):
            if board[r][c]==symbol:
                board[r][c]=-1
                

	
def hint(board):
    r1=0
    c1=0
    r2=1
    c2=0
    for r in range(len(board)-1):
        for c in range(len(board[0])):
            swap(board, r1, c1, r2, c2)
            if vLineAt(board,r1,c1)==True or hLineAt(board,r1,c1)==True or vLineAt(board,r1,c2)==True or hLineAt(board,r2,c2)==True:
                swap(board, r1, c1, r2, c2)
                return r1,c1,r2,c2
            swap(board, r1, c1, r2, c2)
            c1=c1+1
            c2=c2+1
        r1=r1+1
        r2=r2+1
        
    r1=0
    c1=0
    r2=0
    c2=1
    for r in range(len(board)):
        for c in range(len(board[0])-1):
            swap(board, r1, c1, r2, c2)
            if vLineAt(boardr,r1,c1) or hLineAt(board,r1,c1) or vLineAt(board,r2,c2)==True or hLineAt(board,r2,c2)==True:
                swap(board, r1, c1, r2, c2)
                return r1,c1,r2,c2
            swap(board, r1, c1, r2, c2)
            c1=c+1
            c2=c+1
        r1=r+1
        r2=r+1
        
    return -1,-1,-1,-1
