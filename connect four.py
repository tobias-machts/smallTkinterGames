import tkinter as tk

#size of the field where the game is played
rows = 9
columns = 8
#---

turn = 1
grid = []

def neu():
    global turn, grid, gameField, winner, againButton, rows, columns
    turn = 1
    grid = []
    gameField = []
    for y in range(columns):
        grid.append([])
        for x in range(rows):
            gameField.append(field(x, y))
            grid[y].append("_")
    winner.configure(text="")
    againButton.destroy()
    againButton = tk.Label(root, text="", bg="pink")
    againButton.pack(expand=True)

def player():
    if turn%2 == 0:
        return "X", "#ff0000"
    else:
        return "O", "#00ff00"

def selected(x, y):
    playerStats = player()
    gameField[y*rows+x].button.configure(bg = playerStats[1], state = "disabled", text=playerStats[0])
    grid[y][x] = playerStats[0]

def end(text):
    for a in range(len(grid)):
        for b in range(len(grid[0])):
            gameField[a*rows+b].button.configure(state = "disabled")

    global againButton
    winner.configure(text=text)
    againButton.destroy()
    againButton = tk.Button(root, text="Again", command=neu)
    againButton.pack(expand=True)
    for item in gameField:
        item.button.configure(state="disabled")

def  finishCheck():
    gameOver =False
    #win
    if not gameOver:
        #horizontal
        for b in range(len(grid)):
            for a in range(len(grid[b])-3):
                if grid[b][a] == grid[b][a+1] == grid[b][a+2] == grid[b][a+3] and grid[b][a] != "_":
                    gameOver = True
                    end(f"The winner is: {grid[b][a]}!")
    if not gameOver:
        #vertical
        for b in range(len(grid)-3):
            for a in range(len(grid[b])):
                if grid[b][a] == grid[b+1][a] == grid[b+2][a] == grid[b+3][a] and grid[b][a] != "_":
                    gameOver = True
                    end(f"The winner is: {grid[b][a]}!")
    if not gameOver:
        #right-down
        for b in range(len(grid)-3):
            for a in range(len(grid[b])-3):
                if grid[b][a] == grid[b+1][a+1] == grid[b+2][a+2] == grid[b+3][a+3] and grid[b][a] != "_":
                    gameOver = True
                    end(f"The winner is: {grid[b][a]}!")
    if not gameOver:
        #left-down
        for b in range(len(grid) - 3):
            for a in range(3, len(grid[b])):
                if grid[b][a] == grid[b+1][a-1] == grid[b+2][a-2] == grid[b+3][a-3] and grid[b][a] != "_":
                    gameOver = True
                    end(f"The winner is: {grid[b][a]}!")

    #Draw
    if not gameOver:
        full = 0
        for i in range(len(grid)):
            try:
                grid[i].index("_")
            except:
                full+=1

        if full == columns:
            end("Draw")

class field():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.button = tk.Button(game, text="_", command=lambda: self.select(), font=12, width=3, height=1)
        self.button.grid(column=x, row=y)

    def select(self):
        row=self.x
        notUsed = 0
        for i in range(columns):
            if grid[i][row] == "_":
                notUsed = i

        selected(row, notUsed)

        finishCheck()

        global turn
        turn += 1



root = tk.Tk()

root.resizable(False, False)
root.geometry("500x400")
root.title("connect four")
root.config(bg="pink")


winner = tk.Label(root, text="", bg="pink")
winner.pack(expand=True)
game=tk.Frame(root,width=75,height=75)
game.pack(expand=True)
againButton = tk.Label(root, text="", bg="pink")
againButton.pack(expand=True)


gameField=[]
for y in range(columns):
    grid.append([])
    for x in range(rows):
        gameField.append(field(x,y))
        grid[y].append("_")

root.mainloop()