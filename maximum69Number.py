# Leetcode 1323

class Solution:
  def maximum69Number (self, num: int) -> int:
    result = ''
    changed = False
    strNum = str(num)

    for i in strNum:
      if not changed and i == '6':
        result += '9'
        changed = True
      else:
        result += i

    return int(result)