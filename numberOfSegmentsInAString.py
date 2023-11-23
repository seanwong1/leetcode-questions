# Leetcode 434

class Solution:
  def countSegments(self, s: str) -> int:
    count = 0
    segments = ' '.join(s.split()).split(' ')

    for segment in segments:
      if segment:
        count += 1

    return count