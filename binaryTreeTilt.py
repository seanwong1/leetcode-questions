# Leetcode 563

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def findTilt(self, root: Optional[TreeNode]) -> int:
    result = 0

    def helper(node):
      nonlocal result

      if not node:
        return 0
      else:
        left = helper(node.left)
        right = helper(node.right)
        result += abs(left - right)
        return node.val + left + right

    helper(root)
    return result