# Leetcode 1758

class Solution:
  def minOperations(self, s: str) -> int:
    sLen = len(s)
    differences = [0, 0]
    current = False

    for i in range(sLen):
      bit = int(s[i])
      if bit != current:
        differences[0] += 1
      if bit == current:
        differences[1] += 1
      current = not current

    return min(differences)