# Leetcode 482

class Solution:
  def licenseKeyFormatting(self, s: str, k: int) -> str:
    s = ''.join(s.split('-'))[::-1]
    counter = 0
    result = ''

    for char in s:
      if counter == k:
        result += '-'
        counter = 0
      if char.isalpha():
        result += char.upper()
        counter += 1
      else:
        result += char
        counter += 1

    return result[::-1]