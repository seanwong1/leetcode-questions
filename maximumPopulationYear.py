# Leetcode 1854

from typing import List

class Solution:
  def maximumPopulation(self, logs: List[List[int]]) -> int:
    populations = {}

    for birth, death in logs:
      for year in range(birth, death):
        if not year in populations:
          populations[year] = 1
        else:
          populations[year] += 1

    return min([year for year, population in populations.items() if population == max(populations.values())])