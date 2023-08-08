# Leetcode 102

from collections import deque

def levelOrder(root):
  traverse = []
  queue = deque()

  if root:
    queue.append(root)

  while queue:
    storage = []

    for i in range(len(queue)):
      leaf = queue.popleft()
      if leaf.left:
        queue.append(leaf.left)
      if leaf.right:
        queue.append(leaf.right)
      storage.append(leaf.val)

    traverse.append(storage)

  return traverse