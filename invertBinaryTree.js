// Leetcode 226

var invertTree = function(root) {
  var storage = [];
  var temp;
  var swap;
  if (!root) {
    return root;
  }
  storage.push(root);
  while (storage.length) {
    swap = storage.pop();
    if (!swap.left && !swap.right) {
      continue;
    }
    if (swap.left) {
      storage.push(swap.left);
    }
    if (swap.right) {
      storage.push(swap.right);
    }
    temp = swap.left;
    swap.left = swap.right;
    swap.right = temp;
  }
  return root;
};