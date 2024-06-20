# Leetcode 1614

class Solution:
  def maxDepth(self, s: str) -> int:
    max_depth = 0
    storage = []

    for char in s:
      if char == "(":
        storage.append(char)
        max_depth = max(max_depth, len(storage))
      elif char == ")":
        storage.pop()

    return max_depth