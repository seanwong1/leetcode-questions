# Leetcode 238

def productExceptSelf(nums):
  result = [None] * len(nums)
  prefix = [1] * len(nums)
  suffix = [1] * len(nums)

  for i in range(1, len(nums)):
    prefix[i] = prefix[i - 1] * nums[i - 1]

  for i in range(len(nums) - 2, -1, -1):
    suffix[i] = suffix[i + 1] * nums[i + 1]

  for i in range(len(nums)):
    result[i] = prefix[i] * suffix[i]

  return result