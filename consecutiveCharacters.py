# Leetcode 1446

class Solution:
  def maxPower(self, s: str) -> int:
    prev = ''
    result = 0

    for letter in s:
      if letter == prev:
        count += 1
      else:
        count = 1
      prev = letter
      result = max(count, result)

    return result