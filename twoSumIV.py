# Leetcode 653

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    storage = {}

    def helper(node):
      if not node:
        return
      elif k - node.val in storage:
        return True
      else:
        storage[node.val] = k - node.val
        return helper(node.left) or helper(node.right)

    if helper(root):
      return True
    return False