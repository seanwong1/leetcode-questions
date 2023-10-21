# Leetcode 232

class MyQueue:
  def __init__(self):
    self.stackOne = []
    self.stackTwo = []

  def push(self, x: int) -> None:
    self.stackOne.append(x)

  def pop(self) -> int:
    while len(self.stackOne):
      self.stackTwo.append(self.stackOne.pop())

    popped = self.stackTwo.pop()

    while len(self.stackTwo):
      self.stackOne.append(self.stackTwo.pop())

    return popped

  def peek(self) -> int:
    if not len(self.stackOne):
      return None
    else:
      return self.stackOne[0]

  def empty(self) -> bool:
    return self.peek() == None