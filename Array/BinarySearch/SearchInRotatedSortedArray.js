function binarySearch(arr, target) {
  let start = 0;
  let end = arr.length - 1;
  let mid = ~~((start + end) / 2);
  while (start <= end) {
    if (arr[mid] === target) {
      return mid;
    }

    if (target > arr[mid]) start = mid + 1;

    if (target < arr[mid]) end = mid - 1;

    mid = ~~((start + end) / 2);
  }

  mid = -1;
  return mid;
}

function getPivot(arr) {
  let start = 0;
  let end = arr.length - 1;
  let mid = ~~((start + end) / 2);
  while (start < end) {
    if (arr[mid] > arr[0]) {
      start = mid + 1;
    }
    if (arr[mid] < arr[arr.length - 1]) {
      end = mid;
    }
    mid = ~~((start + end) / 2);
  }
  return mid;
}

function searchInRotateArray(arr, target) {
  let pivot = getPivot(arr);
  let searchArray;
  if (arr[pivot] <= target && target <= arr[arr.length - 1]) {
    searchArray = arr.splice(pivot);
    return binarySearch(searchArray, target);
  } else {
    searchArray = arr.splice(0, pivot);
    return binarySearch(searchArray, target);
  }
}

let arr = [7, 9, 10, 1, 2, 3, 4];
let target = 10;

console.log(searchInRotateArray(arr, target));
