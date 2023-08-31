class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  insert(value) {
    var newNode = new Node(value);
    var currentNode = this.root;
    if (!currentNode) {
      this.root = newNode;
      return this;
    } else {
      while (true) {
        if (value === currentNode.value) {
          return undefined;
        }
        if (value > currentNode.value) {
          if (!currentNode.right) {
            currentNode.right = newNode;
            return this;
          } else {
            currentNode = currentNode.right;
          }
        } else if (value < currentNode.value) {
          if (!currentNode.left) {
            currentNode.left = newNode;
            return this;
          } else {
            currentNode = currentNode.left;
          }
        }
      }
    }
  }

  find(value) {
    var currentNode = this.root;
    while (true) {
      if (!currentNode) {
        return undefined;
      }
      if (value === currentNode.value) {
        return currentNode;
      } else if (value < currentNode.value) {
        currentNode = currentNode.left;
      } else if (value > currentNode.value) {
        currentNode = currentNode.right;
      }
    }
  }

  breadthFirstSearch(value) {
    var queue = [];
    var storage = [];
    queue.push(this.root);
    while (queue.length > 0) {
      storage.push(queue.shift());
      if (storage[storage.length - 1].left) {
        queue.push(storage[storage.length - 1].left);
      }
      if (storage[storage.length - 1].right) {
        queue.push(storage[storage.length - 1].right);
      }
    }
    return storage;
  }

  depthFirstSearchPreOrder(value) {
    var storage = [];
    var current = this.root;
    var helper = function(current) {
      storage.push(current);
      if (current.left) {
        helper(current.left);
      }
      if (current.right) {
        helper(current.right);
      }
    }
    helper(current);
    return storage;
  }

  depthFirstSearchPostOrder(value) {
    var storage = [];
    var current = this.root;
    var helper = function(current) {
      if (current.left) {
        helper(current.left);
      }
      if (current.right) {
        helper(current.right);
      }
      storage.push(current);
    }
    helper(current);
    return storage;
  }

  depthFirstSearchInOrder(value) {
    var storage = [];
    var current = this.root;
    var helper = function(current) {
      if (current.left) {
        helper(current.left);
      }
      storage.push(current);
      if (current.right) {
        helper(current.right);
      }
    }
    helper(current);
    return storage;
  }
}