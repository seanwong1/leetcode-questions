# Leetcode 200

def numIslands(grid):
  islands = 0

  for row in range(len(grid)):
    for column in range(len(grid[row])):
      if grid[row][column] == '1':
        islands += 1
        landToCheck = [[row, column]]

        while landToCheck:
          longitude, latitude = landToCheck.pop()
          grid[longitude][latitude] = '2'

          if longitude - 1 >= 0 and grid[longitude - 1][latitude] == '1':
            landToCheck.append([longitude - 1, latitude])
          if longitude + 1 < len(grid) and grid[longitude + 1][latitude] == '1':
            landToCheck.append([longitude + 1, latitude])
          if latitude - 1 >= 0 and grid[longitude][latitude - 1] == '1':
            landToCheck.append([longitude, latitude - 1])
          if latitude + 1 < len(grid[longitude]) and grid[longitude][latitude + 1] == '1':
            landToCheck.append([longitude, latitude + 1])

  return islands