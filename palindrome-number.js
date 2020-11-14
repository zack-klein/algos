/**
 https://leetcode.com/problems/palindrome-number/
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    asStr = x.toString();
    reversed = '';

    for (var i = 0; i < asStr.length; i++){
        end = asStr.length - (i + 1);
        reversed += asStr[end];
    };

    if (reversed == asStr){
        return true
    } else {
        return false
    };
};
