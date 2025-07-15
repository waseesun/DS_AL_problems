/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    i = 0;
    j = needle.length;

    while (j <= haystack.length) {
        if (haystack.slice(i, j) === needle) {
            return i
        }
        i++
        j++
    };

    return -1;
};


console.log(strStr("sadbutsad", "sad"));
console.log(strStr("leetcode", "leeto"));