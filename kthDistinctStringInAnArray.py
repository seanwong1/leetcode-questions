# Leetcode 2053

from typing import List
from collections import Counter

class Solution:
  def kthDistinct(self, arr: List[str], k: int) -> str:
    counter = Counter(arr)
    distinct = ''

    for elem in arr:
      if counter[elem] == 1:
        if k == 1:
          distinct = elem
          return distinct
        else:
          k -= 1

    return distinct