# Leetcode 796

class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
    rotatedString = s

    for offset in range(len(s)):
      rotatedString = rotatedString[1:] + rotatedString[0]
      if rotatedString == goal:
        return True

    return False