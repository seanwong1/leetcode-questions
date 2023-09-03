class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  enqueue(value) {
    var newNode = new Node(value);
    if (this.size === 0) {
      this.first = newNode;
      this.last = newNode;
    } else {
      this.last.next = newNode;
      this.last = newNode;
    }
    this.size++;
    return this;
  }

  dequeue() {
    var toReturn;
    if (this.size === 0) {
      return null;
    } else {
      toReturn = this.first;
      this.first = this.first.next;
      toReturn.next = null;
      this.size--;
      return toReturn;
    }
  }
}

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}