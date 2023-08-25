// Leetcode 543

var diameterOfBinaryTree = function(root) {
  var maxWidth = 0;
  var helper = function(root) {
    var left = 0;
    var right = 0;
    if (!root) {
      return -1;
    }
    left = helper(root.left);
    right = helper(root.right);
    var width = 2 + left + right;
    maxWidth = Math.max(maxWidth, width);
    return 1 + Math.max(left, right);
  }
  helper(root);
  return maxWidth;
};