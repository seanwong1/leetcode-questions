// Leetcode 104

function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

var maxDepth = function(root) {
  var max = 0;
  var helper = function(root, currentLevel, currentLeaf) {
    if (!root.left && !root.right) {
      if (currentLeaf > max) {
        max = currentLeaf;
      }
    } else if (root.left && root.right) {
      helper(root.left, currentLeaf, currentLeaf+1);
      helper(root.right, currentLevel, currentLeaf+1);
    } else if (root.left === null) {
      helper(root.right, currentLevel, currentLeaf+1);
    } else if (root.right === null) {
      helper(root.left, currentLevel, currentLeaf+1);
    }
  }
  if (!root) {
    return max;
  }
  helper(root, 1,1);
  return max;
};