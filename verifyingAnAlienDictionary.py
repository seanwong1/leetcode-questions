# Leetcode 953

from typing import List

class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    letterMap = {}
    for letter in range(26):
      letterMap[order[letter]] = chr(97 + letter)

    for word in range(len(words) - 1):
      if words[word] == words[word + 1]:
        continue

      index = 0
      while words[word][index] and words[word + 1][index]:
        print(words[word][index], words[word + 1][index])
        if words[word][index] == words[word + 1][index]:
          index += 1
          if index >= len(words[word]):
            break
          elif index >= len(words[word + 1]):
            return False
        elif letterMap[words[word][index]] > letterMap[words[word + 1][index]]:
          return False
        else:
          break

    return True

# class Solution:
#   def isAlienSorted(self, words: List[str], order: str) -> bool:
#     letterMap = dict(zip(order, range(len(order))))
#     return sorted(words, key=lambda word: [letterMap[c] for c in word]) == words