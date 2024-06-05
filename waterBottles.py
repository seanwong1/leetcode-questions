# Leetcode 1518

class Solution:
  def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    drank = 0
    emptyBottles = 0

    while numBottles > 0:
      drank += numBottles
      numBottles, finished = divmod(numBottles, numExchange)
      emptyBottles += finished
      exchanged, emptyBottles = divmod(emptyBottles, numExchange)
      numBottles += exchanged

    return drank