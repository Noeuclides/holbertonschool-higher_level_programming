#!/usr/bin/node
const arg = process.argv;
const fs = require('fs');
fs.readFile(arg[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
