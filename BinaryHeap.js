class MaxBinaryHeap {
  constructor() {
    this.values = [];
  }

  insert(value) {
    this.values.push(value);
    var childPos = this.values.length - 1;
    var parentPos = Math.floor((childPos - 1) / 2);
    var temp;
    while (this.values[childPos] > this.values[parentPos]) {
      temp = this.values[parentPos];
      this.values[parentPos] = value;
      this.values[childPos] = temp;
      childPos = parentPos;
      parentPos = Math.floor((childPos - 1) / 2);
    }
    return this;
  }

  extractMax() {
    var max = this.values[0];
    this.values[0] = this.values[this.values.length - 1];
    this.values.pop();
    var parentPos = 0;
    var temp;
    while (parentPos < this.values.length) {
      var child1Pos = (2 * parentPos) + 1;
      var child2Pos = (2 * parentPos) + 2;
      var largerChildPos = (this.values[child1Pos] > this.values[child2Pos] || !this.values[child2Pos]) ? child1Pos : child2Pos;
      if (this.values[largerChildPos] > this.values[parentPos]) {
        temp = this.values[parentPos];
        this.values[parentPos] = this.values[largerChildPos];
        this.values[largerChildPos] = temp;
        parentPos = largerChildPos;
      } else {
        break;
      }
    }
    return max;
  }
}