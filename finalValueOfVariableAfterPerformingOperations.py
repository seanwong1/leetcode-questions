# Leetcode 2011

from typing import List

class Solution:
  def finalValueAfterOperations(self, operations: List[str]) -> int:
    value = 0

    for operation in operations:
      if operation == "X++" or operation == "++X":
        value += 1
      else:
        value -= 1

    return value