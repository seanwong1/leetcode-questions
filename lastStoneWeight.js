// Leetcode 1046

var lastStoneWeight = function(stones) {
  var max1 = -Infinity;
  var max2 = -Infinity;
  if (stones.length === 0) {
    return 0;
  } else if (stones.length === 1) {
    return stones[0];
  } else {
    for (var i = 0; i < stones.length; i++) {
      if (stones[i] >= max1 && stones[i] >= max2) {
        max2 = max1;
        max1 = stones[i];
      } else if (stones[i] >= max2 && stones[i] < max1) {
        max2 = stones[i];
      }
    }
    stones.splice(stones.indexOf(max1), 1);
    stones.splice(stones.indexOf(max2), 1);
    stones.push(max1 - max2);
    return lastStoneWeight(stones);
  }
};