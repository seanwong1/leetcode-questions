# Leetcode 599

from typing import List

class Solution:
  def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    intersection = list(set(list1).intersection(set(list2)))
    storage = {}

    for restaurant in intersection:
      storage[restaurant] = list1.index(restaurant) + list2.index(restaurant)

    return [key for key, value in storage.items() if value == min(storage.values())]