# leetcode 504

class Solution:
  def convertToBase7(self, num: int) -> str:
    result = ''
    sign = 1

    if num < 0:
      sign = -1
      num *= -1
    elif not num:
      return '0'

    while num:
      digit = num % 7
      result = str(digit) + result
      num //= 7

    if sign < 0:
      result = '-' + result

    return result