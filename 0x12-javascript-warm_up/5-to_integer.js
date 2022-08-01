#!/usr/bin/node
const args = process.argv;
if (isNaN(Number(args[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args[2]);
}
