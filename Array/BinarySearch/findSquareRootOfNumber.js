let getPercisionAnswer = (target, temp, percision) => {
  let tempSol = temp;

  let factor = 1;
  for (i = 0; i < percision; i++) {
    factor = factor / 10;

    for (j = tempSol; j * j < target; j += factor) {
      tempSol = parseFloat(j.toFixed(percision));
    }

}
  return tempSol;
};

let findSqrRoot = (num, percision) => {
  let numArray = Array(num)
    .fill(0)
    .map((_, i) => i + 1);

  let start = 0;
  let end = numArray.length - 1;
  let tempSol;

  while (start < end) {
    let mid = ~~((start + end) / 2);
    tempSol = mid;
    let squared = mid * mid;
    if (squared === num) {
      return tempSol;
    }
    if (squared > num) {
      end = mid - 1;
    }
    if (squared < num) {
      tempSol = mid;
      start = mid + 1;
    }
  }

  let answer = getPercisionAnswer(num, tempSol, percision);

  return answer;
};

const number = 37;

console.log("===  findSqrRoot(number):", findSqrRoot(number, 3));
