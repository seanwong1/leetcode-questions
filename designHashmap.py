# Leetcode 706

class MyHashMap:
  def __init__(self, size=2089):
    self.size = size
    self.storage = [[] for i in range(self.size)]

  def hash(self, key: int) -> int:
    return key % self.size

  def put(self, key: int, value: int) -> None:
    hashedKey = self.hash(key)

    for pair in self.storage[hashedKey]:
      if pair[0] == key:
        pair[1] = value
        return

    self.storage[hashedKey].append([key, value])

  def get(self, key: int) -> int:
    hashedKey = self.hash(key)

    for pair in self.storage[hashedKey]:
      if pair[0] == key:
        return pair[1]

    return -1

  def remove(self, key: int) -> None:
    hashedKey = self.hash(key)

    for pair in self.storage[hashedKey]:
      if pair[0] == key:
        self.storage[hashedKey].remove(pair)
        return