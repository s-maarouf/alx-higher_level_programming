#!/usr/bin/node

const myArgs = process.argv.slice(2);
const myNum = parseInt(myArgs[0]);
if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < myNum; i++) {
  console.log('C is fun');
}
