#!/usr/bin/node
const list = require('./100-data').list;
const map1 = list.map(function (item, index) {
  if (index < list.length) {
    return (item * index);
  }
});
console.log(list);
console.log(map1);
