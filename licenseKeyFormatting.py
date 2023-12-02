# Leetcode 482

class Solution:
  def licenseKeyFormatting(self, s: str, k: int) -> str:
    s = ''.join(s.split('-'))[::-1].upper()
    counter = 0
    result = ''

    for char in s:
      if counter == k:
        result += '-'
        counter = 0
      result += char
      counter += 1

    return result[::-1]