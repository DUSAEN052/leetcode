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
var findSecondMinimumValue = function(root) {
    let mySet = new Set();
    let arr = [];
    
    let traverse = function(root) {
        if (root) {
            mySet.add(root.val);
            traverse(root.left);
            traverse(root.right);
        }
    }
    
    traverse(root);
    
    for (let item of mySet) {
        arr.push(item);
    }
    
    arr = arr.sort(function(a, b) {
        return a - b;
    });
    
    if (arr.length == 1 || arr.length == 0) {
        return -1;
    } else {
        return arr[1];
    }
};
