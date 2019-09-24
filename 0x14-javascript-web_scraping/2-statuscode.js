#!/usr/bin/node
const arg = process.argv;
const req = require('request');
req(arg[2], function (error, res) {
  if (error) {
    console.log('code:', res.statusCode);
  } else {
    console.log('code:', res.statusCode);
  }
});
