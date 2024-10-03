# Leetcode 1903

class Solution:
  def largestOddNumber(self, num: str) -> str:
    for i in range(len(num)):
      if int(num[-i - 1]) % 2 == 1:
        return num[0:len(num) - i]

    return ''