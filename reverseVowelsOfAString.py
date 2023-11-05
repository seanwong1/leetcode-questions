# Leetcode 345

class Solution:
  def reverseVowels(self, s: str) -> str:
    vowelStr = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    newStr = [char if not char in vowels else vowelStr.append(char) for char in s]

    vowelStr.reverse()

    for i in range(len(newStr) - 1, -1, -1):
      if newStr[i] == None:
        newStr[i] = vowelStr.pop()

    return ''.join(newStr)