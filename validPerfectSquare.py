# Leetcode 367

class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    if num == 0:
      return True

    i = 1
    while i * i <= num:
      if num % i == 0 and num / i == i:
        return True

      i += 1

    return False