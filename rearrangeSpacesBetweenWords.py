# Leetcode 1592

from collections import Counter

class Solution:
  def reorderSpaces(self, text: str) -> str:
    result = ''
    counter = Counter(text)
    words = ' '.join(text.split()).split(' ')

    if not ' ' in counter:
      return words[0]

    if len(words) == 1:
      return words[0] + (' ' * counter[' '])

    divided = (counter[' ']) // (len(words) - 1)

    for word in words:
      result += word
      if counter[' '] >= divided:
        result += ' ' * divided
        counter[' '] -= divided
      else:
        result += ' ' * counter[' ']
        counter[' '] -= counter[' ']

    while counter[' '] > 0:
      result += ' '
      counter[' '] -= 1

    return result