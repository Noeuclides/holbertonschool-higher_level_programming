#!/usr/bin/node
const arg = process.argv;
const req = require('request');
const URL = 'http://swapi.co/api/films/' + arg[2];
req(URL, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
