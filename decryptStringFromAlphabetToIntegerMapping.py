# Leetcode 1309

class Solution:
  def freqAlphabets(self, s: str) -> str:
    result = ''
    counter = len(s) - 1

    while counter >= 0:
      if s[counter] == '#':
        result += chr(96 + int(s[counter - 2:counter]))
        counter -= 3
      else:
        result += chr(96 + int(s[counter]))
        counter -= 1

    return result[::-1]