# Leetcode 205

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    if not len(s) == len(t):
      return False

    sMap = {}
    tMap = {}

    for i in range(len(t)):
      if not s[i] in sMap:
        sMap[s[i]] = t[i]
      if not t[i] in tMap:
        tMap[t[i]] = s[i]
      if t[i] != sMap[s[i]] or s[i] != tMap[t[i]]:
        return False

    return len(tMap) == len(sMap)