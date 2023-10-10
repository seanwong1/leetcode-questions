# Leetcode 160

from typing import Optional

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    currA = headA
    currB = headB

    while not currA == currB:
      if currA:
        currA = currA.next
      else:
        currA = headB

      if currB:
        currB = currB.next
      else:
        currB = headA

    return currA