#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.

const axios = require('axios');
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    const data = response.data;
    const completed_task = {};
    for (let index = 0; index < data.length; index++) {
      if (data[index].completed === true) {
        if (isNaN(completed_task[data[index].userId])) {
          completed_task[data[index].userId] = 1;
        } else {
          completed_task[data[index].userId] = completed_task[data[index].userId] + 1;
        }
      }
    }
    console.log(completed_task);
  });
