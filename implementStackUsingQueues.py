# Leetcode 225

from collections import deque

class MyStack:
  def __init__(self):
    self.queueOne = deque()
    self.queueTwo = deque()

  def push(self, x: int) -> None:
    self.queueOne.append(x)

  def pop(self) -> int:
    while len(self.queueOne) > 1:
      self.queueTwo.append(self.queueOne.popleft())

    value = self.queueOne.popleft()
    [self.queueOne, self.queueTwo] = [self.queueTwo, self.queueOne]

    return value

  def top(self) -> int:
    while len(self.queueOne) > 1:
      self.queueTwo.append(self.queueOne.popleft())

    value = self.queueOne[0]
    self.queueTwo.append(self.queueOne.popleft())
    [self.queueOne, self.queueTwo] = [self.queueTwo, self.queueOne]

    return value

  def empty(self) -> bool:
    return len(self.queueOne) == 0