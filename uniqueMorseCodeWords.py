# Leetcode 804

from typing import List

class Solution:
  def uniqueMorseRepresentations(self, words: List[str]) -> int:
    code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    storage = set()

    for word in words:
      morseWord = ''
      for char in word:
        morseWord += code[ord(char) - 97]

      storage.add(morseWord)

    return len(storage)