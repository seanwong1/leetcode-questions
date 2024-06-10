# Leetcode 1556

class Solution:
  def thousandSeparator(self, n: int) -> str:
    result = ''
    numLen = len(str(n))
    places = 0

    for i in range(numLen):
      if places == 3:
        result += '.'
        places = 0
      result += str(n % 10)
      n //= 10
      places += 1

    return result[::-1]