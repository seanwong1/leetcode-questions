# Leetcode 1796

class Solution:
  def secondHighest(self, s: str) -> int:
    result = []

    for char in s:
      if char.isdigit():
        result.append(int(char))

    result = sorted(set(result))

    if len(result) < 2:
      return -1
    else:
      return result[-2]