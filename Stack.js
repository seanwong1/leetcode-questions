class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  push(value) {
    var newNode = new Node(value);
    if (this.size === 0) {
      this.first = newNode;
      this.last = newNode;
    } else {
      var currentNode = this.first;
      this.first = newNode;
      newNode.next = currentNode;
    }
    this.size++;
    return this;
  }

  pop() {
    var toReturn;
    if (this.size === 0) {
      return null;
    } else {
      toReturn = this.first;
      this.first = this.first.next;
      toReturn.next = null;
      this.size--;
    }
    return toReturn;
  }
}

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}