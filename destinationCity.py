# Leetcode 1436

from typing import List

class Solution:
  def destCity(self, paths: List[List[str]]) -> str:
    cities = {}
    destinations = []

    for path in paths:
      city1, city2 = path
      destinations.append(city2)
      if not city1 in cities:
        cities[city1] = 1
      else:
        cities[city1] += 1
      if not city2 in cities:
        cities[city2] = 1
      else:
        cities[city2] += 1

    for destination in destinations:
      if cities[destination] == 1:
        return destination