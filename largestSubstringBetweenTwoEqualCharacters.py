# Leetcode 1624

class Solution:
  def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    first_locations = {}
    result = -1

    for index, letter in enumerate(s):
      if not letter in first_locations:
        first_locations[letter] = index
      else:
        result = max(result, index - first_locations[letter] - 1)

    return result