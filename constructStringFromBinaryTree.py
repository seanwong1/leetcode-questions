# Leetcode 606

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def tree2str(self, root: Optional[TreeNode]) -> str:
    result = ''

    def helper(node):
      nonlocal result
      if not node:
        return
      else:
        result += str(node.val)
        if node.left:
          result += '('
          helper(node.left)
          result += ')'
        elif not node.left and node.right:
          result += '()'
        if node.right:
          result += '('
          helper(node.right)
          result += ')'

    helper(root)
    return result