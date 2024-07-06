# Leetcode 1668

class Solution:
  def maxRepeating(self, sequence: str, word: str) -> int:
    repeats = len(sequence) // len(word)
    found = False

    while repeats > 0 and not found:
      if sequence.find(word * repeats) >= 0:
        found = True
      else:
        repeats -= 1

    return repeats