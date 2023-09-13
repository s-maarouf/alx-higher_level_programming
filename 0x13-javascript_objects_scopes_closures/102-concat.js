#!/usr/bin/node

const fs = require('fs');

const firstfile = fs.readFileSync(process.argv[2]);
const secondfile = fs.readFileSync(process.argv[3]);
fs.writeFileSync(process.argv[4], firstfile + secondfile);
