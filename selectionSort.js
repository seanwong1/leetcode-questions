var selectionSort = function(arr) {
  var min;
  for (var i = 0; i < arr.length; i++) {
    min = i;
    for (var j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[min]) {
        min = j;
      }
    }
    [arr[min], arr[i]] = [arr[i], arr[min]]
  }
  return arr;
}