/**
 * Definition for singly-linked list.
 * https://leetcode.com/problems/add-two-numbers/
 * NOTE: This doesn't pass each test case because of a problem with Javascript
 * float addition (ugh).
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    // Walk through l1
    // Grab the values
    // Reverse them

    // Walk through l2
    // Grab the values
    // Reverse them

    // Add results from 1 and 2
    // Reverse them

    node = l1;
    l1Vals = [];

    while (true) {

        l1Vals.unshift(node.val.toString());

        if (!node.next){
            break
        } else {
            node = node.next
        };
    };

    l1Vals = l1Vals.join(separator='');

    node = l2;
    l2Vals = [];

    while (true) {

        l2Vals.unshift(node.val.toString());

        if (!node.next){
            break
        } else {
            node = node.next
        };
    };

    l2Vals = l2Vals.join(separator='');

    nodesSum = parseInt(l1Vals) + parseInt(l2Vals)
    nodesSumStr = nodesSum.toString()

    var lastNode;
    var rootNode;
    var node;

    for (var i=0; i < nodesSumStr.length; i++){
        // Need to build in reverse order
        end = nodesSumStr.length - (i + 1)
        val = parseInt(nodesSumStr[end])


        node = new ListNode(val);

        if (lastNode) {
            lastNode.next = node;
        } else{
            rootNode = node;
        };

        lastNode = node;
    };

    return rootNode

};
