//
//
//


// Even after writing it in another language this solution doesn't make sense
// to me. Going to revisit again.
/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function(root) {
    var number_of_nodes = 1

    let dfs = function(node) {
        if (!node){
            return 0
        }
        let L = dfs(node.left)
        let R = dfs(node.right)

        number_of_nodes = Math.max(number_of_nodes, L+R+1)

        return Math.max(L, R) + 1
    };

    dfs(root)

    return number_of_nodes - 1

};
