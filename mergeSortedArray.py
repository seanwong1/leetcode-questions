# Leetcode 88

from typing import List

class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    n = n - 1
    m = m - 1
    mergedLength = len(nums1) - 1

    while n >= 0:
      if nums1[m] > nums2[n] and m >= 0:
        [nums1[mergedLength], nums1[m]] = [nums1[m], nums1[mergedLength]]
        m -= 1
      else:
        nums1[mergedLength] = nums2.pop()
        n -= 1
      mergedLength -= 1

    return nums1