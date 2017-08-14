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
let findFrequentTreeSum = function(root) {
    let myMap = new Map()
    let max = 0
    let output = []
    
    let traverse = function(root) {
        if (root) {
            let value = root.val
            let leftv = loop(root.left)
            let rightv = loop(root.right)
            let sum = leftv + rightv + value
            
            if (myMap.has(sum)) {
                myMap.set(sum, myMap.get(sum) + 1)
            } else {
                myMap.set(sum, 1)
            }
            
            return sum
        } else {
            return 0
        }
    }
    
    loop(root)
    
    for (var v of myMap.values()) {
        max = Math.max(max, v)
    }
    for (var k of myMap.keys()) {
        if (myMap.get(k) == max) {
            output.push(k)
        }
    }
    
    return output
};
