# Leetcode 859

class Solution:
  def buddyStrings(self, s: str, goal: str) -> bool:
    if len(goal) != len(s):
      return False

    if s == goal:
      return len(set(s)) < len(goal)

    left = 0
    right = len(s) - 1

    while left < right and s[left] == goal[left]:
      left += 1

    while left < right and s[right] == goal[right]:
      right -= 1

    newString = s[:left] + s[right] + s[left + 1:right] + s[left] + s[right + 1:]
    return newString == goal