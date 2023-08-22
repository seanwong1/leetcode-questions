# Leetcode 211

class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.dictionary = Node()

    def addWord(self, word: str) -> None:
        letter = self.dictionary
        for char in word:
            if not char in letter.children:
                letter.children[char] = Node()

            letter = letter.children[char]

        letter.word = True

    def search(self, word: str) -> bool:

      def helper(letters=self.dictionary, index=0):

        for i in range(index, len(word)):
          if word[i] == '.':
            for letter in letters.children:
              if helper(letters.children[letter], i + 1):
                return True

            return False
          elif word[i] not in letters.children:
            return False
          else:
            letters = letters.children[word[i]]

        return letters.word

      return helper()