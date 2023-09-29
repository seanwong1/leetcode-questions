# Leetcode 83

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return None

    previous = head
    current = previous.next

    while current:
      if previous.val == current.val:
        previous.next = current.next
        current = current.next
      else:
        previous = current
        current = current.next

    return head