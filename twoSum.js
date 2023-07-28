var twoSum = function(nums, target) {
  var numsTabl = {};
  for (var i = 0; i < nums.length; i++) {
    if (Object.keys(numsTabl).includes(JSON.stringify(target - nums[i]))) {
        return [i, numsTabl[target - nums[i]]];
    }
    numsTabl[nums[i]] = i;
  }
};