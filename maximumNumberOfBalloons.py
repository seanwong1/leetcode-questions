# Leetcode 1189

from collections import Counter

class Solution:
  def maxNumberOfBalloons(self, text: str) -> int:
    counter = Counter(text)
    balloons = 0

    while all(char in counter for char in ['b', 'a', 'l', 'o', 'n']):
      if all(counter[char] > 0 for char in ['b', 'a', 'n']):
        if all(counter[char] > 1 for char in ['l', 'o']):
          balloons += 1
          counter['b'] -= 1
          counter['a'] -= 1
          counter['l'] -= 2
          counter['o'] -= 2
          counter['n'] -= 1
        else:
          break
      else:
        break

    return balloons