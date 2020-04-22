import tkinter as tk

def ucitajSliku(x):
  ret = tk.PhotoImage(file=x)
  return ret

def ucitaj(imeFajla):
    strana = loadImage(imeFajla)
    pozadina = tk.PhotoImage()
    pozadina.tk.call(pozadina, 'copy', strana, '-from', 0, 0, 800, 600, '-to', 0, 0)

    slike = []
    s_slike = []
    x = 600
    for i in range(7):
        slike.append(tk.PhotoImage())
        slike[-1].tk.call(slike[-1], 'copy', strana, '-from', 0, x, 50, x+50, '-to', 0, 0)
        x += 50

        s_slike.append(tk.PhotoImage())
        s_slike[-1].tk.call(s_slike[-1], 'copy', strana, '-from', 0, x, 50, x+50, '-to', 0, 0)
        x += 50

    slike.append(tk.PhotoImage())
    slike[-1].tk.call(slike[-1], 'copy', strana, '-from', 0, x, 50, x+50, '-to', 0, 0)
    s_slike.append(tk.PhotoImage())
    s_slike[-1].tk.call(s_slike[-1], 'copy', strana, '-from', 0, x, 50, x+50, '-to', 0, 0)
    x += 50

    pobeda = tk.PhotoImage()
    pobeda.tk.call(pobeda, 'copy', strana, '-from', 0, x, 400, x+200, '-to', 0, 0)

    poraz = tk.PhotoImage()
    poraz.tk.call(poraz, 'copy', strana, '-from', 0, x+200, 400, x+400, '-to', 0, 0)

    code_crusher1 = tk.PhotoImage()
    code_crusher1.tk.call(code_crusher1, 'copy', strana, '-from', 0, 1750, 379, 1750+44, '-to', 0, 0)

    code_crusher2 = tk.PhotoImage()
    code_crusher2.tk.call(code_crusher2, 'copy', strana, '-from', 0, 1794, 379, 1794+44, '-to', 0, 0)

    return pozadina, slike, s_slike, pobeda, poraz, code_crusher1, code_crusher2

def drawBoard(board, x, y, sr, sc, slike, s_slike):
    background("black")
    len1 = len(board)
    len2 = len(board[r])

    for r in range(len1):
        for c in range(len2):
        if r == sr and c == sc and board[r][c] != -1:
            drawImage(s_slike[board[sr][sc]], x + sc * 50, y + sr * 50)
        else:
            drawItem(board[r][c], x + c * 50, y + r * 50, slike)