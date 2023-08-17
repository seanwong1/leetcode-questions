// Leetcode 206

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