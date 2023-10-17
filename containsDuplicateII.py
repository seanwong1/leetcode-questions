# Leetcode 219

from typing import List

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    if not k:
      return False

    dups = {}

    for i in range(len(nums)):
      if nums[i] in dups and abs(i - dups[nums[i]]) <= k:
        return True
      dups[nums[i]] = i

    return False