#!/usr/bin/node
let a = Number(process.argv[2]);

if (isNaN(a)) {
  a = 1;
}
function factorial (x) {
  if (x === 0 || x === 1) {
    return (1);
  }
  const y = x * factorial((x - 1));
  return (y);
}
console.log(factorial(a));
