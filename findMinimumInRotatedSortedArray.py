# Leetcode 153

def findMin(nums):
  minimum = nums[0]
  left = 0
  right = len(nums) - 1

  while left <= right:
      midpoint = (right + left) // 2
      minimum = minimum if minimum < nums[midpoint] else nums[midpoint]
      if nums[midpoint] > nums[right]:
         left = midpoint + 1
      else:
         right = midpoint - 1
  return minimum

print(findMin([4,5,6,7,0,1,2]))