# Leetcode 965

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
    storage = []

    def helper(node):
      if not node:
        return
      else:
        helper(node.left)
        storage.append(node.val)
        helper(node.right)


    helper(root)
    return all(node == storage[0] for node in storage)