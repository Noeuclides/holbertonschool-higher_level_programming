#!/usr/bin/node
const Square = require('./5-square');

class newSquare extends Square {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }
}

module.exports = newSquare;
