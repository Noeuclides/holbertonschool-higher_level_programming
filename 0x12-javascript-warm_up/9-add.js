#!/usr/bin/node
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

if (isNaN(a)) {
  console.log(a);
} else if (isNaN(b)) {
  console.log(b);
} else {
  add(a, b);
}

function add (a, b) {
  console.log(a + b);
}
