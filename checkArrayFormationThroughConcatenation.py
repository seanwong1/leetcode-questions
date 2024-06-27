# Leetcode 1640

from typing import List

class Solution:
  def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
    pieceMap = {}
    result = []

    for piece in pieces:
      pieceMap[piece[0]] = piece

    for num in arr:
      if num in pieceMap:
        result += pieceMap[num]

    if len(arr) != len(result):
      return False

    for i in range(len(arr)):
      if arr[i] != result[i]:
        return False

    return True