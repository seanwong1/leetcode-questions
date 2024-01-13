# Leetcode 671

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
    nums = []
    storage = [root]
    while storage:
        node = storage.pop()
        nums.append(node.val)
        if node.left:
            storage.append(node.left)
        if node.right:
            storage.append(node.right)

    return sorted(set(nums))[1] if len(set(nums)) != 1 else -1