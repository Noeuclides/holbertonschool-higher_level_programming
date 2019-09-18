#!/usr/bin/node
const len = process.argv.length;
const a = [];

if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    a.push(process.argv[i]);
  }
  a.sort(function (a, b) { return a - b; });
  console.log(a[a.length - 2]);
}
