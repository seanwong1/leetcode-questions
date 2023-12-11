# Leetcode 507

class Solution:
  def checkPerfectNumber(self, num: int) -> bool:
    if num == 1:
      return False
    result = 1

    for divisor in range(2, int(num ** (1 / 2)) + 1):
      if num % divisor == 0:
        result += divisor
        result += num // divisor

    return result == num