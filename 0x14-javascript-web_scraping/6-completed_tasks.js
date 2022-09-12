#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.

const axios = require('axios');
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    const data = response.data;
    const completedTask = {};
    for (let index = 0; index < data.length; index++) {
      if (data[index].completed === true) {
        if (isNaN(completedTask[data[index].userId])) {
          completedTask[data[index].userId] = 1;
        } else {
          completedTask[data[index].userId] = completedTask[data[index].userId] + 1;
        }
      }
    }
    console.log(completedTask);
  });
