# Leetcode 1560

from typing import List

class Solution:
  def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
    current = rounds[0]
    moves = 0
    sectors = {}

    for i in range(1, n + 1):
      sectors[i] = 0
    sectors[current] = 1

    for i in range(len(rounds) - 1):
      moves += (rounds[i + 1] - rounds[i] + n) % n

    while moves:
      current += 1
      if current > n:
        current = 1
      sectors[current] += 1
      moves -= 1

    most_visited = []
    max_visited = max(sectors.values())

    for key, values in sectors.items():
      if values >= max_visited:
        most_visited.append(key)

    return most_visited