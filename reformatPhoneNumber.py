# Leetcode 1694

class Solution:
  def reformatNumber(self, number: str) -> str:
    nums = []
    result = ''
    count = 0

    for char in number:
      if not char == ' ' and not char == '-':
        nums.append(char)

    length = len(nums)

    while length:
      if length > 4 or length == 3:
        for i in range(3):
          result += nums[count + i]
        if length > 4:
          result += '-'
        length -= 3
        count += 3
      elif length == 4:
        result += nums[count]
        result += nums[count + 1] + '-'
        result += nums[count + 2] + nums[count + 3]
        length -= 4
        count += 4
      elif length == 2:
        result += nums[count] + nums[count + 1]
        length -= 2
        count += 2

    return result