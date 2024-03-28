# Leetcode 1089

from typing import List

class Solution:
  def duplicateZeros(self, arr: List[int]) -> None:
    index = 0
    storage = []

    while index < len(arr):
      if not arr[index]:
        storage.append(0)
      storage.append(arr[index])
      index += 1

    for i in range(len(arr)):
      arr[i] = storage[i]