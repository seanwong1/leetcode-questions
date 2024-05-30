# Leetcode 1496

class Solution:
  def isPathCrossing(self, path: str) -> bool:
    x, y = 0, 0
    storage = set()
    storage.add((x, y))

    for direction in path:
      if direction == 'N':
        y += 1
      if direction == 'S':
        y -= 1
      if direction == 'W':
        x -= 1
      if direction == 'E':
        x += 1

      if (x, y) in storage:
        return True
      else:
        storage.add((x, y))

    return False