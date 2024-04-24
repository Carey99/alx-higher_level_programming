#!/usr/bin/node
const req = require('req');
req.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
