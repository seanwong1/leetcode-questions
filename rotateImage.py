# Leetcode 48

def rotate(matrix):
  for layer in range(len(matrix) // 2):
    start = layer
    end = len(matrix) - 1 - layer

    for i in range(start, end):
      offset = i - start
      top = matrix[start][i]
      matrix[start][i] = matrix[end - offset][start]
      matrix[end - offset][start] = matrix[end][end - offset]
      matrix[end][end - offset] = matrix[i][end]
      matrix[i][end] = top