# Leetcode 290

class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split(' ')
    storage = {}

    if len(pattern) != len(words):
      return False

    for i in range(len(pattern)):
      if pattern[i] in storage:
        if storage[pattern[i]] != words[i]:
          return False
      else:
        if words[i] in storage.values():
          return False

        storage[pattern[i]] = words[i]

    return True