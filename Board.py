import board

class Board():
  def __init__(self, rows, columns, world):
    self.board = board.Board((rows, columns))
    for x in range(len(world)):
      for y in range(len(world[x])):
        if world[x][y] == 0:
          self.board[y, x] = ' '
        else:
          self.board[y, x] = 'X'