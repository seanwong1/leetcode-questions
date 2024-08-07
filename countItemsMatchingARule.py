# Leetcode 1773

from typing import List

class Solution:
  def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    if ruleKey == 'type':
      ruleKey = 0
    elif ruleKey == 'color':
      ruleKey = 1
    else:
      ruleKey = 2

    result = [item[ruleKey] == ruleValue for item in items]
    return sum(result)