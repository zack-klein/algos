//
// https://leetcode.com/problems/majority-element/
//

// One pass hash table
var majorityElement = function(nums) {
    var hashTable = {};
    var majorityMin = nums.length / 2;

    for (var i = 0; i < nums.length; i++){
        current = nums[i];
        count = hashTable[current] || 0;
        count += 1;

        if (count > majorityMin) {
            return current
        }

        hashTable[current] = count;

    }
};


// Boyer-Moore Voting Algorithm
var majorityElementBoyerMoore = function(nums) {
    var count = 0;
    var candidate = null;

    for (var i = 0; i < nums.length; i++){
        let current = nums[i];

        if (count === 0){
            candidate = current;
        }

        let toAdd;
        if (candidate === current){
            toAdd = 1;
        } else {
            toAdd = -1;
        }

        count += toAdd;
    }
    return candidate
};
