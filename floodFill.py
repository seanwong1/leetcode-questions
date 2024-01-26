# Leetcode 733

from typing import List

class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    originalColor = image[sr][sc]

    def helper(row, col):
      if image[row][col] != originalColor:
        return
      else:
        image[row][col] = color
        if row - 1 >= 0:
          helper(row - 1, col)
        if row + 1 < len(image):
          helper(row + 1, col)
        if col - 1 >= 0:
          helper(row, col - 1)
        if col + 1 < len(image[row]):
          helper(row, col + 1)

    if originalColor == color:
      return image
    helper(sr, sc)
    return image