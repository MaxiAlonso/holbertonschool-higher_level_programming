#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.

const axios = require('axios');
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    const films = response.data.results;
    let count = 0;
    for (let idx in films) {
      const characters = films[idx].characters;
      for (let index in characters) {
        if (characters[index] === 'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  });
