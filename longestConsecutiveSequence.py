# Leetcode 128

def longestConsecutive(nums):
  if not len(nums):
    return 0
  nums = set(nums)
  result = 1
  length = 1

  for num in nums:
    if not (num - 1) in nums:
      length = 1
      while num + length in nums:
        length += 1
      result = length if length > result else result

  return result

nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
print(longestConsecutive(nums))