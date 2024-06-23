# Leetcode 1629

from typing import List

class Solution:
  def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
    longest_duration = 0
    press = 0
    result = ''

    for index, release in enumerate(releaseTimes):
      duration = release - press
      if duration == longest_duration:
        result = max(result, keysPressed[index])
      elif duration > longest_duration:
        result = keysPressed[index]
        longest_duration = duration
      press = release

    return result