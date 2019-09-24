#!/usr/bin/node
exports.esrever = function (list) {
  let newList = [];
  let len = list.length;
  for (i = 0; i < len; i++){
    newList.push(list.pop());
  }
  return (newList);
}
