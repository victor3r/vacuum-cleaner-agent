import tkinter as tk

class Board():
  def __init__(self, world, root):
    self.world = world
    self.root = root
    for i in range(len(self.world)):
      for j in range(len(self.world[i])):
        if self.world[i][j] == 0:
          tk.Label(self.root, text='    ', bg='grey').grid(row=i, column=j, ipadx=20, ipady=20, padx=10, pady=10)
        else:
          tk.Label(self.root, text='####', bg='grey').grid(row=i, column=j, ipadx=20, ipady=20, padx=10, pady=10)

