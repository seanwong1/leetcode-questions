# Leetcode 145

from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    storage = [root]
    while storage:
      node = storage.pop()
      if node:
        result.append(node.val)
        storage.append(node.left)
        storage.append(node.right)

    return result[::-1]