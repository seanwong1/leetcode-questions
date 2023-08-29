# Leetcode 230

from typing import *

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    result = []
    def helper(node):
      if not node:
        return
      else:
        if node.left:
          helper(node.left)

        result.append(node.val)

        if node.right:
          helper(node.right)

    helper(root)
    return result[k - 1]