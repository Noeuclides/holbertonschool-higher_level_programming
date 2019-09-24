#!/usr/bin/node
const arg = process.argv;
const fs = require('fs');
const req = require('request');
req(arg[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(arg[3], body, (err) => {
      if (err) console.log(err);
    });
  }
});
