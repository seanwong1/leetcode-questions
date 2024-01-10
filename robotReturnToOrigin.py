# Leetcode 657

class Solution:
  def judgeCircle(self, moves: str) -> bool:
    location = [0, 0]

    for move in moves:
      if move == 'R':
        location[0] += 1
      elif move == 'L':
        location[0] -= 1
      elif move == 'U':
        location[1] += 1
      elif move == 'D':
        location[1] -= 1

    return location[0] == 0 and location[1] == 0