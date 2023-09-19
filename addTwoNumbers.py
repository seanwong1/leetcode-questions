# Leetcode 2

from typing import *

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    result = ListNode()
    current = result

    while l1 or l2 or carry:
      num = carry

      if l1:
        num += l1.val
      if l2:
        num += l2.val

      current.next = ListNode(num % 10)
      carry = num // 10

      current = current.next
      l1 = None if not l1 else l1.next
      l2 = None if not l2 else l2.next

    return result.next