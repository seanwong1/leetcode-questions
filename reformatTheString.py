# Leetcode 1417

class Solution:
  def reformat(self, s: str) -> str:
    result = ''
    nums = []
    alphas = []

    for char in s:
      if char.isnumeric():
        nums.append(char)
      else:
        alphas.append(char)

    if abs(len(alphas) - len(nums)) > 1:
      return result

    switch = len(alphas) > len(nums)
    while nums or alphas:
      result += alphas.pop() if switch else nums.pop()
      switch = not switch

    return result