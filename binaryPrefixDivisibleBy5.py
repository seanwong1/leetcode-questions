# leetcode 1018

from typing import List

class Solution:
  def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
    result = [None] * len(nums)
    counter = len(nums) - 1
    bitStr = ''.join(str(bit) for bit in nums)

    while bitStr:
      result[counter] = int(bitStr, 2) % 5 == 0
      bitStr = bitStr[:-1]
      counter -= 1

    return result