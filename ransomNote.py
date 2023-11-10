# Leetcode 383

class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    letters = {}

    for letter in magazine:
      if not letter in letters:
        letters[letter] = 1
      else:
        letters[letter] += 1

    for letter in ransomNote:
      if not letter in letters or letters[letter] == 0:
        return False
      else:
        letters[letter] -= 1

    return True