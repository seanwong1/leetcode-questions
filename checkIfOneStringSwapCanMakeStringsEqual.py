# Leetcode 1790

class Solution:
  def areAlmostEqual(self, s1: str, s2: str) -> bool:
    if s1 == s2:
      return True

    differences = []

    for i in range(len(s1)):
      if s1[i] != s2[i]:
        differences.append(i)

    if len(differences) != 2:
      return False

    swapped = s2[:differences[0]] + s2[differences[1]] + s2[differences[0] + 1:differences[1]] + s2[differences[0]] + s2[differences[1] + 1:]
    return s1 == swapped