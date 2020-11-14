/**
Find the two indices in an array where the sum adds up to the target.
https://leetcode.com/problems/two-sum/submissions/

 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

    var hashTable = {}

    for (var i = 0; i < nums.length; i++) {

        let complement = target - nums[i]

        if (complement in hashTable){
            complementIndex = hashTable[complement]
            return [i, complementIndex]
        } else {
            hashTable[nums[i]] = i
        }

    };
};
