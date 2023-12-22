# Leetcode 559

class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

class Solution:
  def maxDepth(self, root: 'Node') -> int:
    depth = 0

    if not root:
      return depth

    def helper(node, level):
      nonlocal depth
      if not node.children:
        if level > depth:
          depth = level
      else:
        for child in node.children:
          helper(child, level + 1)

    helper(root, 1)

    return depth