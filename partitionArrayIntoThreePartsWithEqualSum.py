# Leetcode 1013

from typing import List

class Solution:
  def canThreePartsEqualSum(self, arr: List[int]) -> bool:
    goalSum = sum(arr) // 3
    leftSum = 0
    rightSum = 0
    middleSum = 0

    for left in range(len(arr)):
      leftSum += arr[left]
      if leftSum == goalSum:
        break

    for right in range(len(arr) - 1, -1, -1):
      rightSum += arr[right]
      if right - 1 <= left:
        return False
      elif rightSum == goalSum:
        break

    for middle in range(left + 1, right):
      middleSum += arr[middle]

    if leftSum == rightSum == middleSum:
      return True

    return False