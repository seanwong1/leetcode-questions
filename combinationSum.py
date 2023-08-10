# Leetcode 39

def combinationSum(candidates, target):
  result = []
  def helper(index, target, current = []):
    if target == 0:
      result.append(current.copy())
      return
    if target < 0 or index < 0:
      return
    else:
      current.append(candidates[index])
      helper(index, target - candidates[index], current)
      current.pop()
      helper(index - 1, target, current)

  helper(len(candidates) - 1, target)
  return result