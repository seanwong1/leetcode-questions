# leetcode 1805

class Solution:
  def numDifferentIntegers(self, word: str) -> int:
    number = ''
    result = set()

    for index, char in enumerate(word):
      if char.isdigit():
        number += char
      if number and (char.isalpha() or index == len(word) - 1):
        result.add(int(number))
        number = ''

    return len(result)