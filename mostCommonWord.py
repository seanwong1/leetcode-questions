# Leetcode 819

from typing import List
import re

class Solution:
  def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    cleaned = re.sub(r"\s+", ' ', re.sub(r"[!?',;.]+", ' ', paragraph)).lower().split(' ')
    storage = {}

    for word in cleaned:
      if word in storage:
        storage[word] += 1
      elif word == '':
        continue
      else:
        storage[word] = 1

    for word in banned:
      if word in storage:
        storage[word] *= -1

    return max(storage, key=storage.get)