# Leetcode 203

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    current = head
    previous = head

    while current:
      if current.val == val:
        if current.val == previous.val:
          head = head.next
        else:
          previous.next = current.next
      else:
        previous = current
      current = current.next

    return head