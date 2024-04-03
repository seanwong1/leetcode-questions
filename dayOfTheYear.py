# Leetcode 1154

class Solution:
  def dayOfYear(self, date: str) -> int:
    result = 0
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    year, month, day = [int(num) for num in date.split('-')]

    if year % 4 == 0:
      if month > 2:
        result += 1

    for i in range(1, month):
      result += months[i]

    result += day

    return result