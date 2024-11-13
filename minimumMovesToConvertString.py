# Leetcode 2027

class Solution:
  def minimumMoves(self, s: str) -> int:
    moves = 0
    counter = 0

    while counter < len(s):
      if s[counter] == 'X':
        moves += 1
        counter += 3
      else:
        counter += 1

    return moves