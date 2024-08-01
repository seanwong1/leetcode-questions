# Leetcode 1742

class Solution:
  def countBalls(self, lowLimit: int, highLimit: int) -> int:
    storage = {}

    for i in range(lowLimit, highLimit + 1):
      digitSum = 0
      while i:
        digitSum += i % 10
        i //= 10

      if not digitSum in storage:
        storage[digitSum] = 1
      else:
        storage[digitSum] += 1

    return max(storage.values())