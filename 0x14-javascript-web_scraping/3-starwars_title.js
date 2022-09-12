#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.

const axios = require('axios');
const args = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];
axios.get(url)
  .then(function (response) {
    console.log(response.data.title);
  });
