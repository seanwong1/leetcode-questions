// Leetcode 703

class MinHeap {
  constructor() {
    this.values = [];
  }

  insert(value) {
    var i = this.values.length;
    this.values.push(value);
      let parentIndex = Math.floor((i + 1) / 2 - 1);
      if (parentIndex < 0) parentIndex = 0;
      let parentVal = this.values[parentIndex];
      const pushedVal = this.values[i];
      while (i > 0 && parentVal > pushedVal) {
        parentIndex = Math.floor((i + 1) / 2 - 1);
        [this.values[i], this.values[parentIndex]] = [this.values[parentIndex], this.values[i]];
        i = parentIndex;
        parentVal = this.values[Math.max(Math.floor((i + 1) / 2 - 1), 0)];
      }
  }

  remove() {
    if (this.values.length <= 1) return this.values.pop();
    const ret = this.values[0];
    let temp = this.values.pop();
    this.values[0] = temp;
    let i = 0;
    while (true) {
      let rightChildIndex = (i + 1) * 2;
      let leftChildIndex = (i + 1) * 2 - 1;
      let lowest = rightChildIndex;
      if (leftChildIndex >= this.values.length && rightChildIndex >= this.values.length) break;
      if (leftChildIndex >= this.values.length) lowest = rightChildIndex;
      if (rightChildIndex >= this.values.length) lowest = leftChildIndex;
      if (!(leftChildIndex >= this.values.length) && !(rightChildIndex >= this.values.length)) {
        lowest = this.values[rightChildIndex] < this.values[leftChildIndex] ? rightChildIndex : leftChildIndex;
      }
      if (this.values[i] > this.values[lowest]) {
        [this.values[i], this.values[lowest]] = [this.values[lowest], this.values[i]];
        i = lowest;
      } else break;
    }
    return ret;
  }
}

var KthLargest = function(k, nums) {
  this.k = k
  this.heap = new MinHeap();

  for (var i = 0; i < nums.length; i++) {
    this.heap.insert(nums[i]);
  }

  while (this.heap.values.length > this.k) {
    this.heap.remove();
  }
};

KthLargest.prototype.add = function(val) {
  this.heap.insert(val);
  if (this.heap.values.length > this.k) {
    this.heap.remove();
  }
  return this.heap.values[0];
};