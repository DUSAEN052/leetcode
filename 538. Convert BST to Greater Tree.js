/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var convertBST = function(root) {
    let sum = 0;
    loop(root);
    return root;
    
        function loop(root) {
        if (root) {    
            loop(root.right);
            let node = root.val;
            root.val = node + sum;
            sum = root.val;
            loop(root.left);
        }
    };
}
