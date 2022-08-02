#!/usr/bin/node
exports.converter = function (base) {
  function myConverter (number) {
    return number.toString(base);
  }
  return myConverter;
};
