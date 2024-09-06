# Leetcode 1844

class Solution:
  def replaceDigits(self, s: str) -> str:
    result = []

    for index, char in enumerate(s):
      if index % 2 == 0:
        result.append(char)
      else:
        result.append(chr(ord(s[index - 1]) + int(char)))

    return ''.join(result)