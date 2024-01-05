# Leetcode 637

from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    result = {}

    def helper(node, depth=0):
      if not node:
        return
      else:
        if not depth in result:
          result[depth] = [node.val]
        else:
          result[depth].append(node.val)
        helper(node.left, depth + 1)
        helper(node.right, depth + 1)

    helper(root)
    return [sum(level )/ len(level) for level in result.values()]