// Leetcode 21

function Node(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}

var mergeTwoLists = function(list1, list2) {
  var current1 = list1;
  var current2 = list2;
  var list3 = new Node();
  var current3 = list3;
  while (current1 || current2) {
    if (!current1) {
      current3.next = current2;
      current2 = current2.next;
    } else if (!current2) {
      current3.next = current1;
      current1 = current1.next;
    } else if (current1.val <= current2.val) {
      current3.next = current1;
      current1 = current1.next;
    } else if (current1.val > current2.val || !current1) {
      current3.next = current2;
      current2 = current2.next;
    }
    current3 = current3.next;
  }
  list3 = list3.next;
  return list3;
};