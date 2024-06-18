# Leetcode 1598

from typing import List

class Solution:
  def minOperations(self, logs: List[str]) -> int:
    storage = []

    for log in logs:
      if log == '../':
        if storage:
          storage.pop()
      elif log == './':
        continue
      else:
        storage.append(log)

    return len(storage)