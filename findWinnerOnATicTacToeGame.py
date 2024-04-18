# Leetcode 1275

from typing import List

class Solution:
  def tictactoe(self, moves: List[List[int]]) -> str:
    playerA = []
    playerB = []
    counter = 0

    for move in moves:
      if counter % 2 == 0:
        playerA.append(move)
      else:
        playerB.append(move)
      counter += 1

    def hasWin(player):
      if [0, 0] in player and [0, 1] in player and [0, 2] in player:
        return True
      elif [1, 0] in player and [1, 1] in player and [1, 2] in player:
        return True
      elif [2, 0] in player and [2, 1] in player and [2, 2] in player:
        return True
      elif [0, 0] in player and [1, 0] in player and [2, 0] in player:
        return True
      elif [0, 1] in player and [1, 1] in player and [2, 1] in player:
        return True
      elif [0, 2] in player and [1, 2] in player and [2, 2] in player:
        return True
      elif [0, 0] in player and [1, 1] in player and [2, 2] in player:
        return True
      elif [0, 2] in player and [1, 1] in player and [2, 0] in player:
        return True
      else:
        return False

    if hasWin(playerA):
      return 'A'
    elif hasWin(playerB):
      return 'B'
    elif len(moves) == 9 and not hasWin(playerA) and not hasWin(playerB):
      return 'Draw'
    else:
      return 'Pending'