// Leetcode 202

var isHappy = function(n, cycleArray = []) {
  if (n === 1) {
      return true;
  } else {
    var nArray = n.toString().split('');
    var sum = 0;
    for (var i = 0; i < nArray.length; i++) {
      sum += Number(nArray[i])**2;
    }
    if (cycleArray.includes(sum)) {
        return false;
    } else {
        cycleArray.push(sum);
        return isHappy(sum, cycleArray);
    }
  }
};