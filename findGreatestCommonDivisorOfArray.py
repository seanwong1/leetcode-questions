# Leetcode 1979

from typing import List
from math import gcd

class Solution:
  def findGCD(self, nums: List[int]) -> int:
    smallest = min(nums)
    greatest = max(nums)

    return gcd(smallest, greatest)