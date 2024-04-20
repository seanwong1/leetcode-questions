# Leetcode 1281

class Solution:
  def subtractProductAndSum(self, n: int) -> int:
    digits = [int(digit) for digit in str(n)]
    product = 1
    numSum = 0

    for digit in digits:
      numSum += digit
      product *= digit

    return product - numSum