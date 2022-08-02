#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const textA = fs.readFileSync(args[2]);
const textB = fs.readFileSync(args[3]);
fs.writeFileSync(args[4], textA + textB);
