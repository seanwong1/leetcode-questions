# Leetcode 2068

class Solution:
  def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
    counter = [0] * 26

    for i in range(len(word1)):
      counter[ord(word1[i]) - 97] += 1
      counter[ord(word2[i]) - 97] -= 1

    return max(counter) < 4 and min(counter) > -4