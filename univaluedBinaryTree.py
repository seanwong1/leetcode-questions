# Leetcode 965

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

    def helper(node):
      if not node:
        return True
      elif node.val != root.val:
        return False
      else:
        return helper(node.left) and helper(node.right)

    return helper(root)