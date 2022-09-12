#!/usr/bin/node
// Script that reads and prints the content of a file.

const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf8', function (error, data) {
  if (error) {
    return console.error(error);
  }
  console.log(data.toString());
});
