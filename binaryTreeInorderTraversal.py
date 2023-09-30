# Leetcode 94

from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    def helper(node: Optional[TreeNode]) -> None:
      if node == None:
        return

      helper(node.left)
      result.append(node.val)
      helper(node.right)

    helper(root)
    return result