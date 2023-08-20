// Leetcode 235

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

var lowestCommonAncestor = function(root, p, q) {
  if (isSubtree(p, q)) {
    return p;
  } else if (isSubtree(q, p)) {
    return q;
  } else {
    var ancestor;
    var current;
    var queue = [root];
    while (queue.length > 0) {
      current = queue.pop();
      if (!isSubtree(current, p) && !isSubtree(current, q)) {
        continue;
      } else if (!isSubtree(current, p) || !isSubtree(current, q)) {
        break;
      }
      if (current.left) {
        ancestor = current;
        queue.push(current.left);
      }
      if (current.right) {
        anceestor = current;
        queue.push(current.right);
      }
    }
    return ancestor;
  }
};