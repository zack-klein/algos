/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBSTWholeTree = function(root, low, high) {
    var dfs = function(node) {

        if (node){
            if (low <= node.val & node.val <= high){
                ans += node.val;
            };
            dfs(node.left);
            dfs(node.right);

        };

    };

    var ans = 0;
    dfs(root)
    return ans
};

var rangeSumBST = function(root, low, high) {
    var dfs = function(node) {

        if (node){
            if (low <= node.val & node.val <= high){
                ans += node.val;
            };

            if (node.val > low){
                dfs(node.left);
            };

            if (node.val < high){
                dfs(node.right);
            };

        };

    };

    var ans = 0;
    dfs(root)
    return ans
};
