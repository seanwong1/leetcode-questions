# Leetcode 1021

class Solution:
  def removeOuterParentheses(self, s: str) -> str:
    result = ''
    groups = []
    group = ''
    openCount = 0
    closeCount = 0

    for char in s:
      group += char
      if char == '(':
        openCount += 1
      elif char == ')':
        closeCount += 1
      if openCount == closeCount:
        groups.append(group)
        group = ''
        openCount = 0
        closeCount = 0

    for group in groups:
      result += group[1:-1]

    return result