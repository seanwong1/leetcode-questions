# Leetcode 700

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    storage = [root]

    while storage:
      node = storage.pop()
      if node == None:
        return
      elif val < node.val:
        storage.append(node.left)
      elif val > node.val:
        storage.append(node.right)
      elif val == node.val:
        return node