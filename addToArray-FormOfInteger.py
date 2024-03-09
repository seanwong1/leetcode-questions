# Leetcode 989

from typing import List
import sys
sys.set_int_max_str_digits(0)

class Solution:
  def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    number = int(''.join(map(str, num)))
    result = number + k
    return [int(digit) for digit in str(result)]