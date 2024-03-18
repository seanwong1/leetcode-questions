# Leetcode 1022

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
    nums = []
    def helper(node, num):
      if node.left == None and node.right == None:
        nums.append(num + str(node.val))
        return

      if node.left:
        helper(node.left, num + str(node.val))
      if node.right:
        helper(node.right, num + str(node.val))

    helper(root, '')
    return sum([int(num, 2) for num in nums])