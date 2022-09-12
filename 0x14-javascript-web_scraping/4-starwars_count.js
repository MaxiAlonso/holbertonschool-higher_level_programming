#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present
const arg = process.argv;
const axios = require('axios');

axios
  .get(arg[2])
  .then(res => {
    let count = 0;
    for (const data of res.data.results) {
      for (const id of data.characters) {
        if (id.endsWith('18/')) {
          count++;
        }
      }
    }
    console.log(count);
  });
