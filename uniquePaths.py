# Leetcode 62

def uniquePaths(m, n):
  paths = [1] * n

  if m == 1 or n == 1:
    return 1

  for row in range(m - 1, 0, -1):
    newPaths = paths.copy()
    for column in range(n - 2, -1, -1):
      newPaths[column] = newPaths[column] + newPaths[column + 1]
    paths = newPaths

  return newPaths[0]