/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */
let binaryTreePaths = function(root) {
    let output = []
    
    if (!root) {
        return output;
    }
    
    let find = function(root, nxt) {
        if (!root.left && !root.right) {
            output.push(nxt + root.val)
        }
        
        if (root.left) {
            find(root.left, nxt + root.val + "->")
        }
        
        if (root.right) {
            find(root.right, nxt + root.val + "->")
        }
    }
    
    find(root, "")
    return output
};
