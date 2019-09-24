#!/usr/bin/node
const arg = process.argv;
const req = require('request');
const URL = arg[2];
let count = 0;
req(URL, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
