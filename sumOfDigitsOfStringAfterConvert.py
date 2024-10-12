# Leetcode 1945

class Solution:
  def getLucky(self, s: str, k: int) -> int:
    num = ''

    for char in s:
      num += str(ord(char) - 96)

    while k:
      num = sum([int(digit) for digit in num])
      num = str(num)
      k -= 1

    return int(num)