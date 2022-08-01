#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const args = process.argv;
if (isNaN(Number(args[2]))) {
  console.log(NaN);
} else if (isNaN(Number(args[3]))) {
  console.log(NaN);
} else {
  console.log(add(Number(args[2]), Number(args[3])));
}
