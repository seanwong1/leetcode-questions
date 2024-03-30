# Leetcode 1108

class Solution:
  def defangIPaddr(self, address: str) -> str:
    defanged = ''

    for char in address:
      if char == '.':
        defanged += '[.]'
      else:
        defanged += char

    return defanged