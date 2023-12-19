# Leetcode 541

class Solution:
  def reverseStr(self, s: str, k: int) -> str:
    sList = [s[i:i + k] for i in range(0, len(s), k)]
    result = ""

    for i in range(0, len(sList)):
      if i % 2 == 0:
        result += sList[i][::-1]
      else:
        result += sList[i]

    return result