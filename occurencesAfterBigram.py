# leetcode 1078

from typing import List

class Solution:
  def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    result = []
    words = text.split(' ')

    for index, word in enumerate(words):
      if word == first:
        if index + 2 < len(words):
          if words[index + 1] == second:
              result.append(words[index + 2])

    return result