# Leetcode 589

from typing import List

class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

class Solution:
  def preorder(self, root: 'Node') -> List[int]:
    if not root:
      return []

    result = [root.val]

    def helper(node):
      if not node.children:
        return
      else:
        for child in node.children:
          result.append(child.val)
          helper(child)

    helper(root)
    return result