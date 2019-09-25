#!/usr/bin/node
const arg = process.argv;
const req = require('request');
const URL = arg[2];
const dictTodo = {};
let count = 0;
let item = 1;
req(URL, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    const todo = JSON.parse(body);
    for (let i = 0; i < todo.length; i++) {
      if (todo[i].userId === item) {
        if (todo[i].completed === true) {
          count += 1;
        }
      } else if (todo[i].userId in dictTodo) {
        if (todo[i].completed === true) {
          dictTodo[item]++;
        }
      } else {
        count = 0;
        item = todo[i].userId;
        if (todo[i].completed === true) {
          count += 1;
        }
      }
      dictTodo[item] = count;
    }
    console.log(dictTodo);
  }
});
