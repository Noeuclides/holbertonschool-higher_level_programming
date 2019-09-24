#!/usr/bin/node
const arg = process.argv;
const req = require('request');
const URL = arg[2];
const dictTodo = {};
let count = 0;
req(URL, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    const todo = JSON.parse(body);
    let item = todo[0].userId;
    for (let i = 0; i < todo.length; i++) {
      if (todo[i].userId === item) {
        if (todo[i].completed === true) {
          count += 1;
        }
        dictTodo[item] = count;
      } else {
        count = 0;
        item = todo[i].userId;
      }
    }
    console.log(dictTodo);
  }
});
