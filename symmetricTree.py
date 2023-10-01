# Leetcode 101

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def helper(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
      if not left and not right:
        return True
      if not left or not right:
        return False
      if left.val == right.val:
        return helper(left.left, right.right) and helper(left.right, right.left)
    return helper(root.left, root.right)