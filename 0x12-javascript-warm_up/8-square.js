#!/usr/bin/node
const x = process.argv[2];
let s = "";

if (process.argv.length < 3 || isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      s += 'X';
    }
    console.log(s);
    s = "";
  }
}
