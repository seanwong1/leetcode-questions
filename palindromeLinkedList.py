# Leetcode 234

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    reverse = None
    currentOne = slow

    while currentOne:
      node = currentOne.next
      currentOne.next = reverse
      reverse = currentOne
      currentOne = node

    currentOne = reverse
    currentTwo = head

    while currentOne:
      if not currentOne.val == currentTwo.val:
        return False
      currentOne = currentOne.next
      currentTwo = currentTwo.next

    return True