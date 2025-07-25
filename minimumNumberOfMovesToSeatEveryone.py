# Leetcode 2037

from typing import List

class Solution:
  def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
    seats.sort()
    students.sort()

    moves = 0

    for i in range(len(seats)):
      moves += abs(seats[i] - students[i])

    return moves