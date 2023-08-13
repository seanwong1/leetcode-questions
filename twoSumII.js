// Leetcode 167

var twoSum = function(numbers, target) {
  var found = false;
  var pointerOne = 0;
  var pointerTwo = numbers.length - 1;
  while (pointerOne < pointerTwo) {
    var sum = numbers[pointerOne] + numbers[pointerTwo]
    if (sum === target) {
      return [pointerOne + 1, pointerTwo + 1];
    } else if (sum < target) {
      pointerOne++;
    } else if (sum > target) {
      pointerTwo--;
    }
  }
  return [];
};