# Leetcode 1379

class TreeNode:
  def __init__(self, x, left=None, right=None):
    self.val = x
    self.left = left
    self.right = right

class Solution:
  def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    if not original:
      return None
    if original == target:
      return cloned
    else:
      return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)