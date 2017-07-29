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
var averageOfLevels = function(root) {
    let output = new Array();
    let queue = new Array();
    
    if (root == null) {
        return output;
    }
    
    queue.push(root);
    
    while (queue.length > 0) {
        let level = [];
        let sum = 0; 
        let count = 0;
        
        while (queue.length > 0) {
            let node = queue.shift();
            sum += node.val;
            count ++;
            
            if (node.left) {
                level.push(node.left);
            }
            if(node.right) {
                level.push(node.right);
            }
        }
        output.push(sum / count);
        count = 0;
        queue = level;
    }
    
    return output;    
};
