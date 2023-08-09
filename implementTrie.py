# Python 208

class Node:
  def __init__(self):
    self.children = [None] * 26
    self.isWord = False

class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, word: str) -> None:
    letter = self.root
    for char in word:
      index = ord(char) - ord("a")
      if not letter.children[index]:
        letter.children[index] = Node()
      letter = letter.children[index]
    letter.isWord = True

  def search(self, word: str) -> bool:
    letter = self.root
    for char in word:
      index = ord(char) - ord("a")
      if letter.children[index]:
        letter = letter.children[index]
      else:
        return False
    return letter.isWord

  def startsWith(self, prefix: str) -> bool:
    letter = self.root
    for char in prefix:
      index = ord(char) - ord("a")
      if letter.children[index]:
        letter = letter.children[index]
      else:
        return False
    return True