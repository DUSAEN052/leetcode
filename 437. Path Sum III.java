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
    public int pathSum(TreeNode root, int sum) {
        if(root == null) {
            return 0;
        }
        return move(root, sum) + pathSum(root.left, sum) + pathSum(root.right,sum);
    }
    
    public int move(TreeNode root, int sum) {
        int val = 0;
        if (root == null) {
            return 0;
        }
        if (root.val == sum) {
            val += 1;
        }
        val += move(root.left, sum - root.val);
        val += move(root.right, sum - root.val);

        return val;
    }
}
