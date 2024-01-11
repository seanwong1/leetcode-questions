# Leetcode 661

from typing import List

class Solution:
  def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
    IMG_HEIGHT = len(img)
    IMG_WIDTH = len(img[0])
    blurred = [[0 for col in range(IMG_WIDTH)] for row in range(IMG_HEIGHT)]
    for row in range(IMG_HEIGHT):
      for col in range(len(img[row])):
        total = img[row][col]
        count = 1
        if row - 1 >= 0 and col - 1 >= 0:
          total += img[row - 1][col - 1]
          count += 1
        if row - 1 >= 0:
          total += img[row - 1][col]
          count += 1
        if row - 1 >= 0 and col + 1 < IMG_WIDTH:
          total += img[row - 1][col + 1]
          count += 1
        if col - 1 >= 0:
          total += img[row][col - 1]
          count += 1
        if col + 1 < IMG_WIDTH:
          total += img[row][col + 1]
          count += 1
        if row + 1 < IMG_HEIGHT and col - 1 >= 0:
          total += img[row + 1][col - 1]
          count += 1
        if row + 1 < IMG_HEIGHT:
          total += img[row + 1][col]
          count += 1
        if row + 1 < IMG_HEIGHT and col + 1 < IMG_WIDTH:
          total += img[row + 1][col + 1]
          count += 1

        blurred[row][col] = total // count

    return blurred