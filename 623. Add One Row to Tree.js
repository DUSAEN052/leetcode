/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} v
 * @param {number} d
 * @return {TreeNode}
 */
let addOneRow = function(root, v, d) {
    let node = root
    
    let dfs = function(root, depth, v, d) {
        if (root == null) {
            return null
        }
        
        if (depth == d - 1) {
            let tempL = root.left
            let tempR = root.right
            root.left = new TreeNode(v)
            root.right = new TreeNode(v)
            root.left.left = tempL
            root.right.right = tempR
        } else {
            dfs(root.left, depth + 1, v, d)
            dfs(root.right, depth + 1, v, d)
        }
    }
    
    if (d == 1) {
        let nod = new TreeNode(v)
        nod.left = node
        return nod
    }
    
    dfs(node, 1, v, d)
    return node
};
