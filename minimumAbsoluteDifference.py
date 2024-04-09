# Leetcode 1200

from typing import List
import math

class Solution:
  def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr.sort()
    result = []
    minimum = math.inf

    for i in range(len(arr) - 1):
      if arr[i + 1] - arr[i] < minimum:
        minimum = arr[i + 1] - arr[i]
        result = [[arr[i], arr[i + 1]]]
      elif arr[i + 1] - arr[i] == minimum:
        result.append([arr[i], arr[i + 1]])

    return result