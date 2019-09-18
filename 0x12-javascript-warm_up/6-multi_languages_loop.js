#!/usr/bin/node
const myArray = ['C is fun', 'Python is cool', 'Javascript is amazing'];
myArray.forEach(printFunc);

function printFunc (val) {
  console.log(val);
}
