# Leetcode 917

class Solution:
  def reverseOnlyLetters(self, s: str) -> str:
    newString = list(s)
    storage = []
    index = 0

    for char in s:
      if char.isalpha():
        storage.append(char)

    while storage:
      if newString[index].isalpha():
        newString[index] = storage.pop()
      index += 1

    return ''.join(newString)