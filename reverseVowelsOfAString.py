# Leetcode 345

class Solution:
  def reverseVowels(self, s: str) -> str:
    newStr = [None] * len(s)
    pointer1 = 0
    pointer2 = len(s) - 1
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    while pointer1 <= pointer2:
      if s[pointer1] in vowels and s[pointer2] in vowels:
        newStr[pointer1] = s[pointer2]
        newStr[pointer2] = s[pointer1]
        pointer1 += 1
        pointer2 -= 1
      elif not s[pointer1] in vowels:
        newStr[pointer1] = s[pointer1]
        pointer1 += 1
      elif not s[pointer2] in vowels:
        newStr[pointer2] = s[pointer2]
        pointer2 -= 1

    return ''.join(newStr)