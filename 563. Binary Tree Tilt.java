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
    int tilt = 0;
    public int findTilt(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = sub(root.left);
        int right = sub(root.right);
        
        int abs = Math.abs(left - right);
        return abs + tilt;
    }
    
    public int sub(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = sub(root.left);
        int right = sub(root.right);
        tilt += Math.abs(left - right);
        return left + right + root.val;
    }
}
