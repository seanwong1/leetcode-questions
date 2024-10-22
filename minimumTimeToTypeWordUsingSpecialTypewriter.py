# Leetcode 1974

class Solution:
  def minTimeToType(self, word: str) -> int:
    current = 0
    count = 0

    for char in word:
      letter = ord(char) - 97
      dist = abs(letter - current)

      if not letter == current:
        count += min(dist, 26 - dist)

      count += 1
      current = letter

    return count