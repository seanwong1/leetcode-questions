# Leetcode 1137

class Solution:
  def tribonacci(self, n: int) -> int:
    tribonaccis = [0, 1, 1]

    def helper(n):
      if n < len(tribonaccis):
        return tribonaccis[n]
      else:
        tribonaccis.append(helper(n - 1) + helper(n - 2) + helper(n - 3))
        return tribonaccis[n]

    return helper(n)