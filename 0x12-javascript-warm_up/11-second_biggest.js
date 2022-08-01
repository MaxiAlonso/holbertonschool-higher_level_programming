#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const array = [];
  for (let i = 2; i < args.length; i++) {
    array.push(Number(args[i]));
  }
  const index = array.indexOf(Math.max(...array));
  array.splice(index, 1);
  console.log(Math.max(...array));
}
