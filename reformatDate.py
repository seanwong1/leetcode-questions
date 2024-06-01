# Leetcode 1507

from datetime import datetime

class Solution:
  def reformatDate(self, date: str) -> str:
    day, month, year = date.split(' ')
    date = ' '.join([day[:-2], month, year])
    return datetime.strptime(date, '%d %b %Y').strftime('%Y-%m-%d')