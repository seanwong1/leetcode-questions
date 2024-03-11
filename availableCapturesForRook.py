# Leetcode 999

from typing import List

class Solution:
  def numRookCaptures(self, board: List[List[str]]) -> int:
    found = False
    captures = 0
    counter = 1

    for row in range(8):
      for col in range(8):
        if board[row][col] == 'R':
          found = True
          break
      if found:
        break

    while row - counter >= 0:
      if board[row - counter][col] == 'B':
        break
      elif board[row - counter][col] == 'p':
        captures += 1
        break
      else:
        counter += 1

    counter = 1
    while row + counter < 8:
      if board[row + counter][col] == 'B':
        break
      elif board[row + counter][col] == 'p':
        captures += 1
        break
      else:
        counter += 1

    counter = 1
    while col - counter >= 0:
      if board[row][col - counter] == 'B':
        break
      elif board[row][col - counter] == 'p':
        captures += 1
        break
      else:
        counter += 1

    counter = 1
    while col + counter < 8:
      if board[row][col + counter] == 'B':
        break
      elif board[row][col + counter] == 'p':
        captures += 1
        break
      else:
        counter += 1

    return captures