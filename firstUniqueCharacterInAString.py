# Leetcode 387

class Solution:
  def firstUniqChar(self, s: str) -> int:
    storage = {}

    for i in range(len(s)):
      if s[i] in storage:
        storage[s[i]][0] += 1
      else:
        storage[s[i]] = [1, i]

    for value in storage.values():
      if value[0] == 1:
        return value[1]

    return -1