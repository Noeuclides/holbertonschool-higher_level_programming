#!/usr/bin/node
exports.converter = function (base) {
  return function (n) {
    if (base === 10) {
      return (n);
    }
  };
};
