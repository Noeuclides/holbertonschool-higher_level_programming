#!/usr/bin/node
const d = require('./101-data').dict;
const newDict = {};
const list = [];
for (const item in d) {
  list.push(item);
  newDict[d[item]] = list;
}
console.log(newDict);
