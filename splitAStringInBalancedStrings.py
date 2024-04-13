# Leetcode 1221

class Solution:
  def balancedStringSplit(self, s: str) -> int:
    left = []
    right = []
    result = 0

    for char in s:
      if char == 'L':
        left.append('L')
      else:
        right.append('R')
      if len(left) == len(right):
        result += 1
        left = []
        right = []

    return result