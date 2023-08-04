// Leetcode 100

function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

var isSameTree = function(p, q) {
  if (!p && !q) {
    return true;
  } else if (!p || !q) {
    return false;
  } else if (p.val !== q.val) {
    return false;
  } else {
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
  }
};