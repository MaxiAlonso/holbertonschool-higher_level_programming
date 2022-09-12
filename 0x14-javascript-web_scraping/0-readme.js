#!/usr/bin/node
const fs = require('fs').promises;

const args = process.argv;
async function readFile (filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    console.log(data.toString());
  } catch (error) {
    console.dir(error);
  }
}

readFile(args[2]);
