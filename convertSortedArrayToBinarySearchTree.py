# Leetcode 108

from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    if not nums:
      return None
    else:
      midpoint = len(nums) // 2
      return TreeNode(nums[midpoint], self.sortedArrayToBST(nums[0:midpoint]), self.sortedArrayToBST(nums[midpoint + 1:len(nums)]))