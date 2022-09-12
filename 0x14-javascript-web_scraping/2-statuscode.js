#!/usr/bin/node
// Script that display the status code of a GET request.

const axios = require('axios');
const args = process.argv;

axios.get(args[2])
  .then(function (response) {
    console.log('Code: ' + response.status);
  })
  .catch(function (error) {
    console.log('Code: ' + error.response.status);
  });
