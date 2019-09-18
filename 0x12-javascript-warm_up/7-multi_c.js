#!/usr/bin/node
const x = process.argv[2];

if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
