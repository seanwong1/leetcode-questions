# Leetcode 1360

from datetime import date

class Solution:
  def daysBetweenDates(self, date1: str, date2: str) -> int:
    date1 = date.fromisoformat(date1)
    date2 = date.fromisoformat(date2)

    return abs(date2 - date1).days