# Leetcode 728

from typing import List

class Solution:
  def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    result = []

    for num in range(left, right + 1):
      if self.isSelfDividingNumber(num):
        result.append(num)

    return result

  def isSelfDividingNumber(self, num):
    digits = [int(digit) for digit in str(num)]

    for digit in digits:
      if not digit or not num % digit == 0:
        return False

    return True