'use strict';

var isArray = require('is-array');

var forceItem = function(v) {
  return isArray(v) ? v : (v ? [v] : []);
};

var forceArray = function() {
  if (Object.keys(arguments).length <=  1) {
    return forceItem(arguments[0]);
  }

  var firstItem = forceItem(arguments[0]);
  Array.prototype.shift.call(arguments);
  return firstItem.concat(forceArray.apply(null, arguments));
};

module.exports = forceArray;
module.exports.item = forceItem;