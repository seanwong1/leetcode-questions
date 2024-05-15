# Leetcode 1399

class Solution:
  def countLargestGroup(self, n: int) -> int:
    counter = [0] * 37

    for num in range(1, n + 1):
      numSum = 0
      while num:
        num, remainder = divmod(num, 10)
        numSum += remainder

      counter[numSum] += 1

    return counter.count(max(counter))