# Leetcode 415

class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    carry = 0
    result = ''

    if len(num2) > len(num1):
      [num1, num2] = [num2, num1]

    counter = -1

    while abs(counter) <= len(num2):
      digit1 = ord(num1[counter]) - ord('0')
      digit2 = ord(num2[counter]) - ord('0')

      digitSum = digit1 + digit2 + carry
      carry = digitSum // 10

      result = f"{digitSum % 10}{result}"
      counter -= 1

    while abs(counter) <= len(num1):
      digit1 = ord(num1[counter]) - ord('0')

      digitSum = digit1 + carry
      carry = digitSum // 10

      result = f"{digitSum % 10}{result}"
      counter -= 1

    if carry:
      result = f"{carry}{result}"

    return result