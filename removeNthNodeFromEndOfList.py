# Leetcode 19

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def removeNthFromEnd(head, n):
  current = head
  ahead = head
  previous = head

  if head.next == None:
    return None

  while n > 0:
    ahead = ahead.next
    n -= 1

  if ahead == None:
    head = head.next

  while ahead != None:
    previous = current
    current = current.next
    ahead = ahead.next

  if current.next == None:
    previous.next = None
  else:
    previous.next = current.next

  return head