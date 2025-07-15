/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  parenthesis_obj = {
    ')': '(',
    '}': '{',
    ']': '['
  };

  stack = [];

  for (let i = 0; i < s.length; i++) {
    if (')}]'.includes(s[i])) {
      val = stack.pop();
      if (val !== parenthesis_obj[s[i]]) {
        return false
      };
    } else {
      stack.push(s[i])
    }
  };

  if (stack.length > 0) {
    return false
  }
  return true
};

console.log(isValid('()'));
console.log(isValid('(){}[]'));
console.log(isValid('['));
console.log(isValid('(([]))'));
console.log(isValid('(())}'))