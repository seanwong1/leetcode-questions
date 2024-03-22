# Leetcode 1047

class Solution:
  def removeDuplicates(self, s: str) -> str:
    result = []
    counter = 0

    while counter < len(s):
      if len(result) and result[-1] == s[counter]:
        result.pop()
      else:
        result.append(s[counter])
      counter += 1

    return ''.join(result)