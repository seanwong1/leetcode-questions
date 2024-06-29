# Leetcode 1652

from typing import List

class Solution:
  def decrypt(self, code: List[int], k: int) -> List[int]:
    length = len(code)
    storage = [0] * length

    if k == 0:
      return storage

    code = code * 2

    if k < 0:
      for i in range(length):
        storage[i] = sum([code[i - j] for j in range(1, abs(k) + 1)])
    else:
      for i in range(length):
        storage[i] = sum(code[i + 1: i + 1 + k])

    return storage