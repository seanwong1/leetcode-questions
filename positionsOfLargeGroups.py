# Leetcode 830

from typing import List

class Solution:
  def largeGroupPositions(self, s: str) -> List[List[int]]:
    result = [[0, None]]
    current = s[0]

    for index, char in enumerate(s):
      if not char == current:
        result[-1][1] = index - 1
        current = char

        if result[-1][1] - result[-1][0] < 2:
          result.pop()

        result.append([index, None])

    if len(s) - result[-1][0] < 3:
      result.pop()
    else:
      result[-1][1] = len(s) - 1

    return result