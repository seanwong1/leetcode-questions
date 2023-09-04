class Node{
  constructor(val){
    this.val = val;
    this.next = null;
  }
}

class SinglyLinkedList{
  constructor(){
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(val){
    var node = new Node(val)
    if (!this.head) {
      this.head = node;
      this.tail = this.head;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.length++;
    return this;
  }

  traverse() {
    var current = this.head;
    while (current) {
      console.log(current.val);
      current = current.next;
    }
  }

  pop() {
    if (this.length === 0) {
      return undefined;
    }
    var current = this.head;
    var secondLast = current;
    while (current.next) {
      secondLast = current;
      current = current.next;
    }
    var last = this.tail;
    this.tail = secondLast;
    this.tail.next = null;
    this.length--;
    if (this.length === 0) {
      this.head = null;
      this.tail = null;
    }
    return last.val;
  }

  shift() {
    if (this.length === 0) {
      return undefined;
    }
    var removed = this.head;
    this.head = this.head.next;
    this.length--;
    return removed.val;
  }

  unshift(val) {
    var node = new Node(val);
    if (!this.head) {
      this.head = node;
      this.tail = node;
    } else {
      node.next = this.head;
      this.head = node;
    }
    this.length++;
    return this;
  }

  get(index) {
    var current = this.head;
    var counter = 0;
    while (current) {
      if (counter === index) {
        return current;
      }
      current = current.next;
      counter++;
    }
  }

  set(index, value) {
    var found = this.get(index);
    if (found) {
      found.val = value;
      return true;
    }
    return false;
  }

  insert(index, value) {
    if (index > this.length) {
      return this.push(value);
    } else if (index < 0) {
      return this.unshift(value);
    } else {
      var node = new Node(value);
      var currentNode = this.get(index);
      node.next = currentNode.next;
      currentNode.next = node;
      this.length++;
      return this;
    }
  }

  remove(index) {
    if (index >= this.length - 1) {
      return this.pop();
    } else if (index < 1) {
      return this.shift();
    } else {
      var prevNode = this.get(index - 1);
      var toRemove = prevNode.next;
      prevNode.next = toRemove.next;
      toRemove.next = null;
      this.length--;
      return toRemove;
    }
  }

  reverse() {
    var currentNode = this.head;
    var prevNode = null;
    var nextNode = null;
    this.head = this.tail;
    this.tail = currentNode;
    while (currentNode) {
      nextNode = currentNode.next;
      currentNode.next = prevNode;
      prevNode = currentNode;
      currentNode = nextNode;
    }
  }
}