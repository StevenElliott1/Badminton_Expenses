import tkinter as tk
from tkinter import ttk

class CostLabels(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Player cost labels
        self.labelPlayerName = tk.Label(self, text="Player Name")
        self.labelPlayerCourtCost = tk.Label(self, text="Court Cost")
        self.labelPlayerShuttleType = ttk.Label(self, text="Shuttle Type")
        self.labelPlayerShuttleNum = tk.Label(self, text="Number of Shuttles")
        self.labelPlayerTotCost = tk.Label(self, text="Total Cost")

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.labelPlayerName.grid(row=0, column=0, sticky="nsew")
        self.labelPlayerCourtCost.grid(row=1, column=0, sticky="nsew")
        self.labelPlayerShuttleType.grid(row=2, column=0, sticky="nsew")
        self.labelPlayerShuttleNum.grid(row=3, column=0, sticky="nsew")
        self.labelPlayerTotCost.grid(row=4, column=0, sticky="nsew")

class PlayersDisplay(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Initial button to add players

        # self.grid_rowconfigure(0, weight=1)
        # self.costLabel = tk.Frame(self)
        # self.playerView = tk.Frame(self)

        # self.costLabel.grid(row=0, column=0)
        # self.costLabel.grid(row=0, column=0)

        self.subframes = []
        self.topFrame = tk.Frame(self)
        self.groupOfFrames = tk.Frame(self)
        self.topFrame.pack(side="right")
        self.groupOfFrames.pack(side="left")

        self.add = tk.Button(self.topFrame, text="ADD PLAYER", command=self.addFrame)
        self.add.pack(side="right")
        
    def deleteFrame(self, frame):
        self.subframes.remove(frame)
        frame.destroy()

    def addFrame(self):
        f = PlayerFrame(parent=self.groupOfFrames, controller=self)
        self.subframes.append(f)
        f.pack(side="left", fill="x")

# PlayerFrame class defines a frame of input boxes for each player
class PlayerFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        
        # Player widgets
        self.playerName = tk.Entry(self)
        self.playerRemoveButton = tk.Button(self, text="-", command=self.removePlayer)
        self.playerCourtCost = tk.Entry(self)
        self.playerShuttleType = ttk.Combobox(self)
        self.playerShuttleNum = tk.Entry(self)
        self.PlayerTotCost = tk.Label(self)

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.playerName.grid(row=0, column=0, sticky="nsew")
        self.playerRemoveButton.grid(row=0, column=1, sticky="w")
        self.playerCourtCost.grid(row=1, column=0, sticky="nsew")
        self.playerShuttleType.grid(row=2, column=0, sticky="nsew")
        self.playerShuttleNum.grid(row=3, column=0, sticky="nsew")
        self.PlayerTotCost.grid(row=4, column=0, sticky="nsew")

        # Define each input widget box

    # Removes this player from the window
    def removePlayer(self):
        self.controller.deleteFrame(self)

# Encompasses
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.parent.geometry("400x400")

        # Setup a grid and place each container frame into the correct location



        # Add the view of players to the main window
        self.grid_rowconfigure(0, weight=1)
        self.costDetails = CostLabels(self).grid(row=0, column=0, sticky="nsew")
        
        self.playerView = PlayersDisplay(self).grid(row=0, column=1, sticky="nsew")

        


def main():
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()
