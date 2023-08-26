// Leetcode 572

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

var isSubtree = function(root, subRoot) {
  if (!root) {
    return false;
  }
  if (isSameTree(root, subRoot)) {
    return true;
  } else {
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
  }
};