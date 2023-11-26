# Leetcode 146

from collections import deque

class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.storage = {}
    self.queue = deque()

  def get(self, key: int) -> int:
    if key in self.storage:
      self.queue.remove(key)
      self.queue.append(key)

      return self.storage[key]

    return -1

  def put(self, key: int, value: int) -> None:
    if key in self.queue:
      self.queue.remove(key)

    self.storage[key] = value
    self.queue.append(key)

    if len(self.queue) > self.capacity:
      del self.storage[self.queue.popleft()]