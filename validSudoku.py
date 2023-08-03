# Leetcode 36

def isValidSudoku(board):
  columns = [[0] * 9 for i in range(9)]
  rows = [[0] * 9 for i in range(9)]
  squares = {
    (0, 0): [0] * 9,
    (0, 1): [0] * 9,
    (0, 2): [0] * 9,
    (1, 0): [0] * 9,
    (1, 1): [0] * 9,
    (1, 2): [0] * 9,
    (2, 0): [0] * 9,
    (2, 1): [0] * 9,
    (2, 2): [0] * 9,
  }

  for row in range(9):
    for column in range(9):
      if board[row][column] == ".":
        continue
      else:
        digit = int(board[row][column]) - 1
      if rows[row][digit] > 0:
        return False
      if columns[column][digit] > 0:
        return False
      if squares[(row // 3, column // 3)][digit] > 0:
        return False

      rows[row][digit] += 1
      columns[column][digit] += 1
      squares[(row // 3, column // 3)][digit] += 1

  return True