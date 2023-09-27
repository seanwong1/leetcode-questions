# Leetcode 67

class Solution:
  def toBinary(self, num: str) -> int:
    result = 0
    for i in range(len(num)):
      if num[len(num) - 1 - i] == '1':
        result += 2 ** i
    return result

  def addBinary(self, a: str, b: str) -> str:
    return str(bin(self.toBinary(a) + self.toBinary(b)))[2:]