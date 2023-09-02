class HashTable {
  constructor(size=53) {
    this.keyMap = new Array(size);
  }

  _hash(key) {
    let total = 0;
    let WEIRD_PRIME = 31;
    for (let i = 0; i < Math.min(key.length, 100); i++) {
      let char = key[i];
      let value = char.charCodeAt(0) - 96;
      total = (total * WEIRD_PRIME + value) % this.keyMap.length;
    }
    return total;
  }

  set(key, value) {
    if (!this.keyMap[this._hash(key)]) {
      this.keyMap[this._hash(key)] = [[key, value]];
    } else {
      this.keyMap[this._hash(key)].push([key, value]);
    }
  }

  get(key) {
    var hashedKey = this._hash(key);
    if (this.keyMap[hashedKey]) {
      for (var i = 0; i < this.keyMap[hashedKey].length; i++) {
        if (this.keyMap[hashedKey][i][0] === key) {
          return this.keyMap[hashedKey][i][1];
        }
      }
    }
    return undefined;
  }

  keys() {
    var keys = [];
    for (var i = 0; i < this.keyMap.length; i++) {
      if (this.keyMap[i]) {
        for (var j = 0; j < this.keyMap[i].length; j++) {
          keys.push(this.keyMap[i][j][0]);
        }
      }
    }
    return keys;
  }

  values() {
    var values = [];
    for (var i = 0; i < this.keyMap.length; i++) {
      if (this.keyMap[i]) {
        for (var j = 0; j < this.keyMap[i].length; j++) {
          values.push(this.keyMap[i][j][1]);
        }
      }
    }
    return values;
  }
}