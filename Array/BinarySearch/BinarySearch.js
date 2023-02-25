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

let arr = [1, 2, 4, 12, 52, 59];
let target = 12;

console.log(binarySearch(arr, target));
