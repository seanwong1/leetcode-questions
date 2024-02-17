# Leetcode 872

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def getLeaves(node):
      storage = ''

      def helper(node):
        nonlocal storage
        if not node.left and not node.right:
          storage += ',' + str(node.val)
        else:
          if node.left:
            helper(node.left)
          if node.right:
            helper(node.right)
      helper(node)
      return storage

    return getLeaves(root1) == getLeaves(root2)