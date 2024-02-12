# Leetcode 844

class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:
    sStorage = []
    tStorage = []

    for char in s:
      if char == '#' and not len(sStorage) == 0:
        sStorage.pop()
      elif char.isalpha():
        sStorage.append(char)

    for char in t:
      if char == '#' and not len(tStorage) == 0:
        tStorage.pop()
      elif char.isalpha():
        tStorage.append(char)

    return ''.join(sStorage) == ''.join(tStorage)