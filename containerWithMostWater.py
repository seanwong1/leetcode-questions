# Leetcode 11

def maxArea(heights):
  left = 0
  right = len(heights) - 1
  most = 0
  height = max(heights)

  while left < right:
    test = min(height[left], height[right]) * (right - left)
    most = test if test >= most else most
    if heights[left] < heights[right]:
      left += 1
    elif heights[left] >= heights[right]:
      right -= 1

  return most