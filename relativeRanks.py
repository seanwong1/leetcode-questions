# Leetcode 506

from typing import List
import heapq

class Solution:
  def findRelativeRanks(self, score: List[int]) -> List[str]:
    storage = []
    ranks = [0] * len(score)
    medals = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}

    for i in range(len(score)):
      heapq.heappush(storage, (score[i], i))

    for i in range(len(storage)):
      num, index = heapq.heappop(storage)
      if len(score) - i in medals:
        ranks[index] = medals[len(score) - i]
      else:
        ranks[index] = str(len(score) - i)

    return ranks