# Leetcode 1812

class Solution:
  def squareIsWhite(self, coordinates: str) -> bool:
    coordinates = list(coordinates)
    col = (ord(coordinates[0]) - 97)
    row = (int(coordinates[1]))

    if col % 2 == 0:
      return row % 2 != 1
    else:
      return row % 2 != 0