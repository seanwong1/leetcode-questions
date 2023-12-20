# Leetcode 551

class Solution:
  def checkRecord(self, s: str) -> bool:
    late = 0
    absence = 0

    for attendance in s:
      if attendance == 'L':
        late += 1
        if late >= 3:
          return False
      elif attendance == 'A':
        absence += 1
        if absence >= 2:
          return False
        late = 0
      else:
        late = 0

    return True