# Leetcod 1576

class Solution:
  def modifyString(self, s: str) -> str:
    sList = list(s)

    for i in range(len(sList)):
      if sList[i] == '?':
        for j in range(26):
          if (i < 0 or not sList[i - 1] == chr(61 + j) and (i + 1 == len(s) or not sList[i + 1] == chr(61 + j))):
            sList[i] = chr(61 + j)
            break

    return ''.join(sList)