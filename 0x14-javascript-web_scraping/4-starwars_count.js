#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.

const argv = process.argv;
const axios = require('axios');

axios.get(argv[2])
  .then(resp => {
    let count = 0;
    for (let idx = 0; resp.data.results[idx]; idx++) {
      if (resp.data.results[idx].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  });
