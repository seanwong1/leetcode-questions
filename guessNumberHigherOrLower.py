# Leetcode 374

class Solution:
  def guessNumber(self, n: int) -> int:
    left = 1
    right = n

    while left <= right:
      mid = (left + right) // 2
      if guess(mid) == 0:
        return mid
      elif guess(mid) == 1:
        left = mid + 1
      else:
        right = mid - 1