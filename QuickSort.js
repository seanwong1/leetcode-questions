var pivot = function(arr, start = 0, end = arr.length - 1) {
  var pivot = start;
  for (var i = start + 1; i <= end; i++) {
    if (arr[start] > arr[i]) {
      pivot++;
      [arr[i], arr[pivot]] = [arr[pivot], arr[i]];
    }
  }
  [arr[start], arr[pivot]] = [arr[pivot], arr[start]];
  return pivot;
}

var quickSort = function(arr, left = 0, right = arr.length - 1) {
  if (left < right) {
    var newPivot = pivot(arr, left, right);
    quickSort(arr, left, newPivot - 1);
    quickSort(arr, newPivot + 1, right);
  }
  return arr;
}