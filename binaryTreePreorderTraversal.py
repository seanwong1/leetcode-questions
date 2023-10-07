# Leetcode 144

from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []

    def helper(node):
      if not node:
        return
      else:
        result.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(root)
    return result