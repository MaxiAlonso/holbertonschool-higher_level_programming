#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.

const axios = require('axios');
const args = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];
axios.get(url)
  .then(function (response) {
    const characters = response.data.characters;
    for (let index = 0; index < characters.length; index++) {
      axios.get(characters[index])
        .then(function (response2) {
          console.log(response2.data.name);
        });
    }
  });
