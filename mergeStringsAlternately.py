# Leetcode 1768

class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    result = ''
    counter1 = 0
    counter2 = 0

    while counter1 < len(word1) and counter2 < len(word2):
      result += word1[counter1]
      result += word2[counter2]
      counter1 += 1
      counter2 += 1

    result += word1[counter1:]
    result += word2[counter2:]

    return result