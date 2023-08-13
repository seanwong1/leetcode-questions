# Leetcode 198

def rob(nums):
  oldMax = 0
  newMax = 0

  for i in range(len(nums)):
    temp = oldMax + nums[i] if oldMax + nums[i] > newMax else newMax
    oldMax = newMax
    newMax = temp

  return newMax