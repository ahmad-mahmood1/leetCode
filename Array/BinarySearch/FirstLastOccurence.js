function firstLastOccurence(arr, target) {


  //keep searching for left most (first) occurence by moving the end pointer to the left on every positive
  let firstOccurence = () => {
    let index;
    let start = 0;
    let end = arr.length - 1;
    while (start <= end) {
      let mid = ~~((start + end) / 2);
      if (arr[mid] === target) {
        index = mid;
        end = mid - 1;
      }

      if (target > arr[mid]) {
        start = mid + 1;
      }
      if (target < arr[mid]) {
        end = mid - 1;
      }
    }
    return index;
  };


  //keep searching for right most (last) occurence by moving the start pointer to the right on every positive
  let lastOccurence = () => {
    let index;
    let start = 0;
    let end = arr.length - 1;
    while (start <= end) {
      let mid = ~~((start + end) / 2);
      if (arr[mid] === target) {
        index = mid;
        start = mid + 1;
      }

      if (target > arr[mid]) {
        start = mid + 1;
      }
      if (target < arr[mid]) {
        end = mid - 1;
      }
    }
    return index;
  };

  return [firstOccurence(), lastOccurence()];
}

let arr = [0, 1, 2, 2, 2, 5];
let target = 2;

console.log(firstLastOccurence(arr, target));
