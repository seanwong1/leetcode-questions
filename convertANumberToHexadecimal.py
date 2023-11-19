# Leetcode 405

class Solution:
  def toHex(self, num: int) -> str:
    hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    result = ''

    if not num:
      return '0'
    elif num < 0:
      num = (1 << 32) + num

    while num > 0:
      digit = num % 16
      result = hexadecimal[digit] + result
      num //= 16

    return result