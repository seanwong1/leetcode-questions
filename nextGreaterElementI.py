# Leetcode 496

from typing import List

class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result = []

    for num1 in range(len(nums1)):
      for num2 in range(len(nums2)):
        isGreater = 1
        if nums1[num1] == nums2[num2]:
          for i in range(num2, len(nums2)):

            if nums2[i] > nums1[num1]:
              result.append(nums2[i])
              isGreater = 0
              break

          if isGreater:
            result.append(-1)

    return result