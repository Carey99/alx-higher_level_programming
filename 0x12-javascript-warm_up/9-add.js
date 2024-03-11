#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const num = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
if (!isNaN(num) && !isNaN(num2)) {
  console.log(add(num, num2));
} else {
  console.log(NaN);
}
