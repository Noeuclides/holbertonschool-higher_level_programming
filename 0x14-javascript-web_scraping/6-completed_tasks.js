#!/usr/bin/node
const arg = process.argv;
const req = require('request');
const URL = arg[2];
req(URL, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    const todo = JSON.parse(body);
    let filt = todo.filter(x => x.completed);
    filt = filt.reduce((accum, current) => {
      accum[current.userId] = accum[current.userId] + 1 || 1;
      return (accum);
    }, {});
    console.log(filt);
  }
});
