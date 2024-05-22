# Leetcode 1437

from typing import List

class Solution:
  def kLengthApart(self, nums: List[int], k: int) -> bool:
    for prev, num in enumerate(nums):
      if num == 1:
        break

    for i in range(prev + 1, len(nums)):
      if nums[i] == 1 and i - prev - 1 < k:
        return False
      elif nums[i] == 1 and i - prev - 1 >= k:
        prev = i

    return True