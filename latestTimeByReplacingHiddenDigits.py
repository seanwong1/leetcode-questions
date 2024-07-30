# Leetcode 1736

class Solution:
  def maximumTime(self, time: str) -> str:
    result = list(time)

    if result[-1] == '?':
      result[-1] = '9'
    if result[-2] == '?':
      result[-2] = '5'
    if result[0] == '?' and result[1] == '?':
      result[0] = '2'
      result[1] = '3'
    elif (result[0] == '1' or result[0] == '0') and result[1] == '?':
      result[1] = '9'
    elif result[0] == '2' and result[1] == '?':
      result[1] = '3'
    elif result[0] == '?' and int(result[1]) > 3:
      result[0] = '1'
    elif result[0] == '?' and int(result[1]) < 4:
      result[0] = '2'

    return ''.join(result)