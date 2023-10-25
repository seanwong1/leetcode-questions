# Leetcode 257

from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    result = []

    def helper(node, string):
      string += str(node.val)

      if not node.left and not node.right:
          result.append(string)
          return

      if node.left:
          helper(node.left, string + '->')

      if node.right:
          helper(node.right, string + '->')

    helper(root, '')
    return result