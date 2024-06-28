# Leetcode 1646

class Solution:
  def getMaximumGenerated(self, n: int) -> int:
    nums = []

    if n >= 0:
      nums.append(0)
    if n >= 1:
      nums.append(1)

    for i in range(2, n + 1):
      if i % 2 == 0:
        nums.append(nums[i // 2])
      else:
        nums.append(nums[i // 2] + nums[i // 2 + 1])

    return max(nums)