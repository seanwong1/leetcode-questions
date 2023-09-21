# Leetcode 13

class Solution:
  def romanToInt(self, s: str) -> int:
    VALUES = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000
    }

    if type(s) != str:
      return None

    decimal = 0
    for i in range(len(s) - 2, -1, -1):
      if VALUES[s[i]] == None:
        return None
      if VALUES[s[i]] < VALUES[s[i + 1]]:
        decimal -= VALUES[s[i]]
      else:
        decimal += VALUES[s[i]]

    return decimal + VALUES[s[-1]]