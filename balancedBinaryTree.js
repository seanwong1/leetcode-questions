// Leetcode 110

var isBalanced = function(root) {
  var helper = function(root) {
    if (!root) {
      return [true, 0];
    }
    var left = helper(root.left);
    var right = helper(root.right);
    var diff = Math.abs(left[1] - right[1]);
    if (left[0] && right[0] && diff <= 1) {
      return [true, 1 + Math.max(left[1], right[1])];
    }
    return [false, 1 + Math.max(left[1], right[1])];
  }
  return helper(root)[0];
}