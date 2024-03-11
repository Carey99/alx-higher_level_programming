#!/usr/bin/node

const square = parseInt(process.argv[2]);

if (!isNaN(square)) {
  for (let i = 0; i < square; i++) {
    let line = '';
    for (let j = 0; j < square; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
