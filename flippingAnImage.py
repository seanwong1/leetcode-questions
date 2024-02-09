# Leetcode 832

from typing import List

class Solution:
  def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    result = []
    for row in image:
      result.append([abs(pixel - 1) for pixel in reversed(row)])

    return result