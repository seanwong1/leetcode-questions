# Leetcode 705

class MyHashSet:
  def __init__(self):
    self.storage = set()

  def add(self, key: int) -> None:
    self.storage.add(key)

  def remove(self, key: int) -> None:
    if self.contains(key):
      self.storage.remove(key)

  def contains(self, key: int) -> bool:
    return self.storage.__contains__(key)