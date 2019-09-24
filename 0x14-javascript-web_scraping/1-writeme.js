#!/usr/bin/node
const arg = process.argv;
const fs = require('fs');
const data = arg[3];
fs.writeFile(arg[2], data, (err) => {
  if (err) console.log(err);
});
