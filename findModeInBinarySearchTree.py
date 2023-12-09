# Leetcode 501

from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def findMode(self, root: Optional[TreeNode]) -> List[int]:
    result = {}
    storage = [root]

    while storage:
      node = storage.pop()
      if node:
        if node.val in result:
          result[node.val] += 1
        else:
          result[node.val] = 1

        storage.append(node.left)
        storage.append(node.right)

    return [key for key in result if result[key] == max(result.values())]