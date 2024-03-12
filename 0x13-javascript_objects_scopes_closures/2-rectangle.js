#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h === undefined || w <= 0 || h <= 0) {
      this;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
