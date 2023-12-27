# Leetcode 590

from typing import List

class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    result = []
    storage = [root]

    if not root:
      return []

    while storage:
      node = storage.pop()

      for child in node.children:
        storage.append(child)

      result.append(node.val)

    return reversed(result)