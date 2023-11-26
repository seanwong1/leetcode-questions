# Leetcode 146

from collections import OrderedDict

class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.storage = OrderedDict()

  def get(self, key: int) -> int:
    value = self.storage.get(key, -1)
    if value != -1:
       self.storage.move_to_end(key)

    return value

  def put(self, key: int, value: int) -> None:
    if key in self.storage:
       self.storage.move_to_end(key)

    self.storage[key] = value

    if len(self.storage) > self.capacity:
       self.storage.popitem(0)