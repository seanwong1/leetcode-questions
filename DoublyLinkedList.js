class Node {
  constructor(value) {
    this.val = value;
    this.prev = null;
    this.next = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(value) {
    var newNode = new Node(value);
    var prevNode;
    if (this.length === 0) {
      this.tail = newNode;
      this.head = newNode;
    } else {
      this.tail.next = newNode;
      newNode.prev = this.tail;
      this.tail = newNode;
    }
    this.length++;
    return this;
  }

  pop() {
    var toRemove = this.tail;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = toRemove.prev;
      toRemove.prev = null;
      this.tail.next = null;
    }
    this.length--;
    return toRemove;
  }

  shift() {
    var toRemove = this.head;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = toRemove.next;
      this.head.prev = null;
      toRemove.next = null;
    }
    this.length--;
    return toRemove;
  }

  unshift(value) {
    var newNode = new Node(value);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.head.prev = newNode;
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length++;
    return this;
  }

  get(index) {
    if (index < 0 || index > this.length - 1) {
      return null;
    } else {
      var counter = 0;
      var currentNode = this.head;
      while (index !== counter) {
        counter++;
        currentNode = currentNode.next;
      }
      return currentNode;
    }

  }

  set(index, value) {
    var currentNode = this.get(index);
    if (currentNode) {
      currentNode.val = value;
      return true;
    }
    return false;
  }

  insert(index, value) {
    if (index < 0) {
      this.unshift(value);
    } else if (index > this.length) {
      this.push(value);
    } else {
      var newNode = new Node(value);
      var currentNode = this.get(index);
      var nextNode = currentNode.next;
      currentNode.next = newNode;
      newNode.prev = currentNode;
      newNode.next = nextNode;
      nextNode.prev = newNode;
    }
    this.length++;
    return this;
  }

  remove(index) {
    if (index < 0) {
      this.shift();
    } else if (index > this.length) {
      this.pop();
    } else {
      var currentNode = this.get(index);
      var prevNode = currentNode.prev;
      var nextNode = currentNode.next;
      currentNode.next = null;
      currentNode.prev = null;
      prevNode.next = nextNode;
      nextNode.prev = prevNode;
    }
    this.length--;
    return this;
  }

  traverse() {
    var current = this.head;
    while (current) {
      console.log(current.val);
      current = current.next;
    }
  }
}