// Leetcode 143

var reverseList = function(head) {
  var current = head;
  var next = null;
  var prev = null;
  head = current;
  var head = head;
  while (current) {
    next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  head = prev;
  return head;
};

var reorderList = function(head) {
  var head2;
  var slow = head;
  var fast = head.next;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  head2 = slow.next;
  slow.next = null;
  head2 = reverseList(head2);
  var current1 = head;
  var current2 = head2;
  var next1;
  var next2;
  while (current1 && current2) {
    next1 = current1.next;
    next2 = current2.next;
    current1.next = current2;
    current2.next = next1;
    current1 = next1;
    current2 = next2;
  }
  return head;
};