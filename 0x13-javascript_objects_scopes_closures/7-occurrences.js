#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occs = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      occs++;
    }
  }
  return occs;
};
