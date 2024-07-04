# Leetcode 1656

from typing import List

class OrderedStream:
  def __init__(self, n: int):
    self.storage = [None] * n
    self.pointer = 0

  def insert(self, idKey: int, value: str) -> List[str]:
    idKey -= 1
    self.storage[idKey] = value
    if idKey > self.pointer:
      return []

    while self.pointer < len(self.storage) and self.storage[self.pointer]:
      self.pointer += 1

    return self.storage[idKey:self.pointer]