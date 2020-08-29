import tkinter as tk
from Board import Board

class VacuumCleaner:
  def __init__(self, world):
    self.time = 1000
    self.world = world
    self.world_columns = self.world.shape[1] - 1
    self.world_rows = self.world.shape[0] - 1
    self.position = {'x': 0, 'y': 0}
    self.cleaned_squares = 0
    self.root = tk.Tk()
    self.root.title('Agente aspirador de pó')
    self.root.after(self.time, lambda: self.root.destroy())
    Board(self.world, self.root)
    self.root.mainloop()

  def aspirate(self):
    for pos in self.world:
      for square in pos:
        if square == 1:
          VacuumCleaner.clean(self)
          self.root = tk.Tk()
          self.root.title('Agente aspirador de pó')
          self.root.after(self.time, lambda: self.root.destroy())
          Board(self.world, self.root)
          self.root.mainloop()
        else:
          print('O bloco da linha: {}, coluna: {} já está limpo!'.format(self.position['x'], self.position['y']))
          print('Indo para o próximo...\n')
        VacuumCleaner.goRight(self)

  def goLeft(self):
    if self.position['x'] == 0 and self.position['y'] == 0:
      return
    elif self.position['y'] == 0 and self.position['x'] > 0:
      self.position['y'] = self.world_columns
      self.position['x'] -= 1
    else:
      self.position['y'] -= 1

  def goRight(self):
    if self.position['x'] == self.world_rows and self.position['y'] == self.world_columns:
      return
    elif self.position['y'] == self.world_columns:
      self.position['y'] = 0
      self.position['x'] += 1
    else:
      self.position['y'] += 1

  def goUp(self):
    if self.position['x'] == 0:
      return
    else:
      self.position['x'] -= 1

  def goDown(self):
    if self.position['x'] == self.world_rows:
      return
    else:
      self.position['x'] += 1

  def clean(self):
      print('O bloco da linha: {}, coluna: {} está sujo!'.format(self.position['x'], self.position['y']))
      print('Aspirando...')
      self.world[self.position['x']][self.position['y']] = 0
      print('Limpeza finalizada!\n')
      self.cleaned_squares += 1

  def getScore(self):
    return self.cleaned_squares