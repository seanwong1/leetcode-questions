# Leetcode 1290

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def getDecimalValue(self, head: ListNode) -> int:
    num = 0
    curr = head

    while curr:
      num = 2 * num + curr.val
      curr = curr.next

    return num