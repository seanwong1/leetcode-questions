# Leetcode 171

class Solution:
  def titleToNumber(self, columnTitle: str) -> int:
    columnNumber = 0

    for letter in columnTitle:
      columnNumber = columnNumber * 26 + (ord(letter) - 64)

    return columnNumber