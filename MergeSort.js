var mergeArrays = function(array1, array2) {
  var i = 0;
  var j = 0;
  var mergedArray = [];
  while (i < array1.length && j < array2.length) {
    if (array1[i] < array2[j]) {
      mergedArray.push(array1[i]);
      i++;
    } else {
      mergedArray.push(array2[j]);
      j++;
    }
  }
  while (i < array1.length) {
    mergedArray.push(array1[i]);
    i++;
  }
  while (j < array2.length) {
    mergedArray.push(array2[j]);
    j++;
  }
  return mergedArray;
}

var mergeSort = function(array) {
  var midpoint = Math.floor(array.length / 2);
  if (array.length <= 1) {
    return array;
  } else {
    var left = mergeSort(array.slice(0, midpoint));
    var right = mergeSort(array.slice(midpoint, array.length));
    return mergeArrays(left, right);
  }
}