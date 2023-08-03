// Leetcode 74

var searchMatrix = function(matrix, target) {
  var rows = matrix.length;
  var cols = matrix[0].length;
  var top = 0;
  var bottom = rows - 1;
  var midpoint;

  while (top <= bottom) {
    midpoint = Math.floor((top + bottom) / 2);
    if (target < matrix[midpoint][0]) {
      bottom = midpoint - 1;
    } else if (target > matrix[midpoint][cols - 1]) {
      top = midpoint + 1;
    } else {
      break;
    }
  }

  if (top > bottom) {
    return false;
  }

  var row = midpoint;
  var left = 0;
  var right = cols - 1;
  while (left <= right) {
    midpoint = Math.floor((left + right) / 2);
    if (target < matrix[row][midpoint]) {
      right = midpoint - 1;
    } else if (target > matrix[row][midpoint]) {
      left = midpoint + 1;
    } else {
      return true;
    }
  }
  return false;
};