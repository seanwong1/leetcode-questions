# Leetcode 496

from typing import List

class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    storage = []
    nextGreater = {}

    for num2 in nums2:
      while storage and storage[-1] < num2:
        nextGreater[storage.pop()] = num2

      storage.append(num2)

    for num1 in nums1:
      if num1 in nextGreater:
        result.append(nextGreater[num1])
      else:
        result.append(-1)

    return result