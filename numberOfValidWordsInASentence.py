# Leetcode 2047

from collections import Counter

class Solution:
  def countValidWords(self, sentence: str) -> int:
    count = 0
    words = sentence.split(' ')
    counter = Counter()

    for word in words:
      isValid = True
      for i, char in enumerate(word):
        if char.isdigit() or (char in '!.,' and i != len(word) - 1):
          isValid = False
          break
        elif char == '-':
          counter = Counter(word)
          if counter['-'] > 1 or i == 0 or i == len(word) - 1 or not word[i + 1].isalpha():
            isValid = False
            break
      if isValid and len(word):
        count += 1

    return count