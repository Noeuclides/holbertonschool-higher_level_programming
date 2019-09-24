#!/usr/bin/node
const arg = process.argv;
const req = require('request');
const URL = arg[2];
let wedge = '';
req(URL, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    const characters = results[0].characters;
    for (let i = 0; i < characters.length; i++) {
      if (characters[i].includes('/18/')) {
        wedge = characters[i];
      }
    }
    const req2 = require('request');
    req2(wedge, function (error, res, body) {
      if (error) {
        console.log(error);
      } else {
        console.log(JSON.parse(body).films.length);
      }
    });
  }
});
