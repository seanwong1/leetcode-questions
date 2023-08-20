# Leetcode 33

def search(nums, target):
  left = 0
  right = len(nums) - 1
  while left <= right:
    midpoint = (right + left) // 2
    if nums[midpoint] == target:
      return midpoint
    if nums[left] < nums[midpoint]:
      if target < nums[left]:
        left = midpoint + 1
      else:
        right = midpoint - 1
    elif nums[midpoint] < nums[right]:
      if target < nums[midpoint]:
        right = midpoint - 1
      else:
        left = midpoint + 1
    else:
      return -1