#!/usr/bin/node
// Script that writes a string to a file.

const fs = require('fs');
const args = process.argv;

fs.writeFile(args[2], args[3], 'utf8', function (error, data) {
  if (error) {
    return console.error(error);
  }
});
