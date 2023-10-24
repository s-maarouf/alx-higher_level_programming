#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) { console.log(err); } else {
    const json = JSON.parse(body);
    const dict = {};
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (dict[json[i].userId] === undefined) {
          dict[json[i].userId] = 1;
        } else {
          dict[json[i].userId] += 1;
        }
      }
    }
    console.log(dict);
  }
});
