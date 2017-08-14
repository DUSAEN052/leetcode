/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
let findBottomLeftValue = function(root) {
    let output = 0
    let queue = []
    
    if (root == null) {
        return 0
    }
    
    queue.push(root)
    
    while (queue.length > 0) {
        let level = []
        let x = 0
        
        while (queue.length > 0) {
            let node = queue.shift()
            x = node.val
            
            if(node.right) {
                level.push(node.right)
            }
            if (node.left) {
                level.push(node.left)
            }
        }
        output = x
        queue = level
    }

    return output
};

