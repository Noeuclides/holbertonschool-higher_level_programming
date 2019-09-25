#!/usr/bin/node
const arg = process.argv;
const req = require('request');
const URL = 'https://swapi.co/api/films/' + arg[2];
req(URL, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).characters;
    for (let i = 0; i < results.length; i++) {
      const req2 = require('request');
      const URL2 = results[i];
      req2(URL2, function (err, r, bod) {
        if (err) {
          console.log(err);
        } else {
          const r = JSON.parse(bod).name;
          console.log(r);
        }
      });
    }
  }
});
