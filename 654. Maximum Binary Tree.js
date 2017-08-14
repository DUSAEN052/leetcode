/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
let constructMaximumBinaryTree = function(nums) {
    if (nums.length === 0) {
        return null
    }
    
    let big = Math.max.apply(Math, nums) //find biggest
    let index = nums.indexOf(big) // get index of biggest
    let node = new TreeNode(big) // root is biggest
    
    node.left = constructMaximumBinaryTree(nums.slice(0, index))
    node.right = constructMaximumBinaryTree(nums.slice(index + 1))
    
    return node
};
