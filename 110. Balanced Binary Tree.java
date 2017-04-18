/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isBalanced(TreeNode root) {
        boolean output = true;
        if (root == null) {
            return true;
        }
        
        if (isBalanced(root.left) == false || isBalanced(root.right) == false || maxHeight(root) == -1){
            return false;
        }
       
        return output;
    }
    
    public int maxHeight(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int left = maxHeight(root.left);
        int right = maxHeight(root.right);
 
        if (Math.abs(left - right) > 1) {
            return -1;
        }
        return Math.max(left, right) + 1;
    }
}
