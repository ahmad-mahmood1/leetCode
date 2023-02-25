function peakMountain(arr) {
  let start = 0;
  let end = arr.length - 1;
  let mid;
  while (start < end) {
    mid = ~~((start + end) / 2);
    if (arr[mid] < arr[mid + 1]) {
      start = mid + 1;
    } else {
      end = mid;
    }
  }
  return mid;
}

let arr = [1, 2, 4, 5, 3, 2];

console.log(peakMountain(arr));
