#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.

const axios = require('axios');
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    const films = response.data.results;
    let count = 0;
    for (let index = 0; index < films.length; index++) {
      const characters = films[index].characters;
      for (let index2 = 0; index2 < characters.length; index2++) {
        if (characters[index2].includes('https://swapi-api.hbtn.io/api/people/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  });
