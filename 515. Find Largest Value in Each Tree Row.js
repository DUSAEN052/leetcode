/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
let largestValues = function(root) {
    let output = []
    let queue = []
    
    if (!root) {
        return []
    }

    if (root == null) {
        return root
    }
    
    queue.push(root)
    output.push(root.val)
    
    while (queue.length > 0) {
        let level = []
        let nums = []
        
        while (queue.length > 0) {
            let node = queue.shift()
            
            if (node.left) {
                level.push(node.left)
                nums.push(node.left.val)
            }
            if (node.right) {
                level.push(node.right)
                nums.push(node.right.val)
            }
        }
        
        if (nums.length > 0) {
            let big = Math.max.apply(Math, nums)
            output.push(big)
        }
        queue = level
    }
    
    return output
};