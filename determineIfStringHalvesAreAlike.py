# Leetcode 1704

class Solution:
  def halvesAreAlike(self, s: str) -> bool:
    s = s.lower()
    storage = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    for index, char in enumerate(s[:len(s) // 2]):
      if char in vowels:
        storage[char] += 1

    for index, char in enumerate(s[len(s) // 2:]):
      if char in vowels:
        storage[char] -= 1

    return sum(storage.values()) == 0