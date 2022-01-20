import tkinter as tk

round = 1
grid = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

def newGame():
    global round, grid, buttons, winner, againButton
    round = 1
    grid = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    buttons = []
    for y in range(3):
        for x in range(3):
            buttons.append(feld(x, y))
    winner.configure(text="")
    againButton.destroy()
    againButton = tk.Label(root, text="", bg="pink")
    againButton.pack(expand=True)



def turn():
    global round
    if round%2 == 0:
        return "X", "#ff0000"
    else:
        return "O", "#00ff00"

class feld:
    def __init__(self, x, y):
        self.button = tk.Button(game, text="_", command=lambda: self.select(), font=12, width=3, height=1)
        self.button.grid(column=x, row=y)
        self.x = x
        self.y = y

    def select(self):
        character = turn()
        self.button.configure(state="disabled", text=character[0], bg=character[1])
        grid[self.y*3+self.x] = character[0]
        #print(grid)
        self.finishCheck()
        global round
        round+=1

    def finishCheck(self):
        if (grid[0] == grid[1] == grid[2] and grid[2] != "_") or (grid[3] == grid[4] == grid[5] and grid[4] != "_") or (grid[6] == grid[7] == grid[8] and grid[7] != "_") or (grid[0] == grid[3] == grid[6] and grid[3] != "_") or (grid[1] == grid[4] == grid[7] and grid[4] != "_") or (grid[2] == grid[5] == grid[8] and grid[5] != "_") or (grid[0] == grid[4] == grid[8] and grid[4] != "_") or (grid[2] == grid[4] == grid[6] and grid[4] != "_"):
            character = turn()
            self.end(f"The winner is '{character[0]}'!")
        else:
            try:
                grid.index("_")
            except:
                self.end("Draw")

    def end(self, text):
        global againButton
        winner.configure(text=text)
        againButton.destroy()
        againButton = tk.Button(root, text="Again", command=newGame)
        againButton.pack(expand=True)
        for item in buttons:
            item.button.configure(state="disabled")



root = tk.Tk()
#root.minsize(width=150, height=150)
root.resizable(False, False)
root.geometry("300x200")
root.title("Tic-Tac-Toe")
root.config(bg="pink")


winner = tk.Label(root, text="", bg="pink")
winner.pack(expand=True)
game=tk.Frame(root,width=75,height=75)
game.pack(expand=True)
againButton = tk.Label(root, text="", bg="pink")
againButton.pack(expand=True)


buttons=[]
for y in range(3):
    for x in range(3):
        buttons.append(feld(x,y))

root.mainloop()