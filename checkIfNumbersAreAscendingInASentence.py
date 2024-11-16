# Leetcode 2042

class Solution:
  def areNumbersAscending(self, s: str) -> bool:
    tokens = s.split(' ')
    current = -1

    for token in tokens:
      if token.isdigit():
        next = int(token)
        if current < next:
          current = next
        else:
          return False

    return True