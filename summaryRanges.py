# Leetcode 228

from typing import List

class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    result = []
    strRange = [None, None]

    if not nums:
      return result

    for num in nums:
      if strRange[0] == None:
        strRange[0] = num
        strRange[1] = num
      elif num == strRange[1] + 1:
        strRange[1] = num
      else:
        if strRange[0] == strRange[1]:
          result.append(str(strRange[0]))
        else:
          result.append(str(strRange[0]) + '->' + str(strRange[1]))
        strRange[0] = num
        strRange[1] = num

    if strRange[0] == strRange[1]:
      result.append(str(strRange[0]))
    else:
      result.append(str(strRange[0]) + '->' + str(strRange[1]))

    return result