class Graph {
  constructor() {
    this.adjacencyList = {};
  }

  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) {
      this.adjacencyList[vertex] = [];
    }
  }

  addEdge(vertex1, vertex2) {
    this.adjacencyList[vertex1].push(vertex2);
    this.adjacencyList[vertex2].push(vertex1);
  }

  removeEdge(vertex1, vertex2) {
    this.adjacencyList[vertex1] = this.adjacencyList[vertex1].filter(v => v !== vertex2);
    this.adjacencyList[vertex2] = this.adjacencyList[vertex2].filter(v => v !== vertex1);
  }

  removeVertex(vertex) {
    var adjacentVertex;
    while (this.adjacencyList[vertex].length) {
      adjacentVertex = this.adjacencyList[vertex].pop();
      this.removeEdge(vertex, adjacentVertex);
    }
    delete this.adjacencyList[vertex];
  }

  depthFirstRecursive(vertex) {
    var results = [];
    var visited = {};
    const adjacencyList = this.adjacencyList;

    var helper = function(vertex) {
      if (!vertex) {
        return;
      }
      results.push(vertex);
      visited[vertex] = true;
      adjacencyList[vertex].forEach(neighbor => {
        if(!visited[neighbor]){
          return helper(neighbor);
        }
      });
    }
    helper(vertex);
    return results;
  }

  depthFirstIterative(start) {
    var stack = [start];
    var visited = {};
    var results = [];
    var vertex;

    while (stack.length) {
      vertex = stack.pop();
      if (!visited[vertex]) {
        results.push(vertex);
        visited[vertex] = true;
        this.adjacencyList[vertex].forEach(neighbor => {
          stack.push(neighbor);
        });
      }
    }
    return results;
  }

  breadthFirstSearch(start) {
    var queue = [start];
    var visited = {};
    var results = [];
    var vertex;

    while (queue.length) {
      vertex = queue.shift();
      if (!visited[vertex]) {
        results.push(vertex);
        visited[vertex] = true;
        this.adjacencyList[vertex].forEach(neighbor => {
          queue.push(neighbor);
        });
      }
    }
    return results;
  }
}