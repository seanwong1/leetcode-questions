# Leetcode 2062

class Solution:
  def countVowelSubstrings(self, word: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    for i in range(len(word) - 4):
      for j in range(i + 5, len(word) + 1):
        if vowels == set(word[i:j]):
          count += 1

    return count