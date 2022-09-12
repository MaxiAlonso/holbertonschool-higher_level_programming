#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

const axios = require('axios');
const fs = require('fs');
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    fs.writeFile(args[3], response.data, 'utf8', function (error, data) {
      if (error) {
        return console.error(error);
      }
    });
  });
