# Leetcode 589

from typing import List

class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

class Solution:
  def preorder(self, root: 'Node') -> List[int]:
    result = []
    storage = []

    if root:
      storage.append(root)

    while storage:
      node = storage.pop()
      result.append(node.val)

      for child in reversed(node.children):
        storage.append(child)

    return result