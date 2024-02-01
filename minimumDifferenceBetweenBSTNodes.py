# Leetcode 783

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    storage = []
    minimum = float('inf')

    def helper(node: Optional[TreeNode]) -> None:
      if node == None:
        return

      helper(node.left)
      storage.append(node.val)
      helper(node.right)

    helper(root)
    storage = sorted(storage)

    for i in range(len(storage) - 1):
      minimum = min(minimum, abs(storage[i] - storage[i + 1]))

    return minimum