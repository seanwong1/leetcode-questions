# Leetcode 14

from collections import Counter

class Solution:
  def maxScore(self, s: str) -> int:
    counter = Counter(s)
    left = 0
    right = counter['1']
    scores = []

    for i in range(1, len(s)):
      if s[i] == '0':
        left += 1
      else:
        right -= 1
      scores.append(left + right)

    return max(scores)