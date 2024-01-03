# Leetcode 617

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 and not root2:
      return

    def helper(node1, node2):
      if not node1 and not node2:
        return
      elif node1 and not node2:
        return node1
      elif node2 and not node1:
        return node2
      else:
        newNode = TreeNode(node1.val + node2.val)
        newNode.left = helper(node1.left, node2.left)
        newNode.right = helper(node1.right, node2.right)
        return newNode

    return helper(root1, root2)