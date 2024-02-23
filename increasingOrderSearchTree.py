# Leetcode 897

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def increasingBST(self, root: TreeNode) -> TreeNode:
    storage = []
    result = TreeNode()
    current = result

    def helper(node):
      if node == None:
        return

      helper(node.left)
      storage.append(node.val)
      helper(node.right)

    helper(root)

    for value in storage:
      current.right = TreeNode(value)
      current = current.right

    return result.right