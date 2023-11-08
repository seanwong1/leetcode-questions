# Leetcode 367

class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    return (num**(1 / 2)).is_integer()