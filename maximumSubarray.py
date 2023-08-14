# Leetcode 53

def maxSubArray(nums):
  result = nums[0]
  total = 0

  for num in nums:
    total += num
    if total > result:
      result = total
    if total < 0:
      total = 0

  return result