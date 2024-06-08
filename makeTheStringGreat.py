# Leetcode 1544

class Solution:
  def makeGood(self, s: str) -> str:
    storage = []
    current = 0

    while current < len(s):
      if storage and abs(ord(storage[-1]) - ord(s[current])) == 32:
        storage.pop()
      else:
        storage.append(s[current])
      current += 1

    return ''.join(storage)