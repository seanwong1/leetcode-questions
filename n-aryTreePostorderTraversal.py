# Leetcode 590

from typing import List

class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    result = []

    def helper(node):
      if not node:
        return
      else:
        for child in node.children:
          helper(child)
        result.append(node.val)

    helper(root)
    return result