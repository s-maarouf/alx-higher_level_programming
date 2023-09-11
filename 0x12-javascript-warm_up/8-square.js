#!/usr/bin/node

const myArgs = process.argv.slice(2);
const myNum = parseInt(myArgs[0]);
if (isNaN(myNum)) {
  console.log('Missing size');
}
for (let i = 0; i < myNum; i++) {
  console.log('X'.repeat(myNum));
}
