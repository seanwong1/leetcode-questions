# Leetcode 15

def threeSum(nums):
  nums.sort()
  result = []

  for i in range(len(nums)):

    if i > 0 and nums[i] == nums[i - 1]:
      continue

    left = i + 1
    right = len(nums) - 1

    while left < right:
      triplet = [nums[left], nums[i], nums[right]]
      total = sum(triplet)
      if total < 0:
        left += 1
      elif total > 0:
        right -= 1
      else:
        result.append(triplet)
        left += 1
        right -= 1
        while nums[left] == nums[left - 1] and left < right:
          left += 1

  return result