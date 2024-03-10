# Leetcode 993

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
    def helper1(node, value):
      if not node:
        return 101
      elif node.val == value:
        return 0
      elif not node.left:
        return helper1(node.right, value) + 1
      elif not node.right:
        return helper1(node.left, value) + 1
      else:
        return min(helper1(node.left, value), helper1(node.right, value)) + 1

    def helper2(node):
      if not node:
        return True
      elif not node.left:
        return helper2(node.right)
      elif not node.right:
        return helper2(node.left)
      elif node.left.val == x and node.right.val == y:
        return False
      elif node.left.val == y and node.right.val == x:
        return False
      else:
        return helper2(node.left) and helper2(node.right)

    return helper2(root) and (helper1(root, x) == helper1(root, y))