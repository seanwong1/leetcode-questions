# Leetcode 938

from typing import *

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
      return 0
    elif root.val < low:
      return self.rangeSumBST(root.right, low, high)
    elif root.val > high:
      return self.rangeSumBST(root.left, low, high)
    else:
      return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)