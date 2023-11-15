# Leetcode 401

from typing import List

class Solution:
  def readBinaryWatch(self, turnedOn: int) -> List[str]:
    result = []

    for hour in range(12):
      for minute in range(60):
        if hour.bit_count() + minute.bit_count() == turnedOn:
          result.append(str(hour) + ':' + str(minute).rjust(2, '0'))

    return result