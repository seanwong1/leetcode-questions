# Leetcode 925

class Solution:
  def isLongPressedName(self, name: str, typed: str) -> bool:
    pName = 0
    pTyped = 0

    if len(name) > len(typed) or set(name) != set(typed):
      return False

    while pName < len(name) and pTyped < len(typed):
      if name[pName] == typed[pTyped]:
        pTyped += 1
        pName += 1
      elif name[pName] != typed[pTyped] and name[pName - 1] == typed[pTyped] and pName - 1 >= 0:
        pTyped += 1
      else:
        return False

    if (pTyped >= len(typed) and pName < len(name)) or (pTyped < len(typed) and typed[pTyped] != name[-1]):
      return False
    return True