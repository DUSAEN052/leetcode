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
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode tmpl = root.left;
        TreeNode tmpr = root.right;
        root.left = tmpr;
        root.right = tmpl;
         
        invertTree(root.left);
        invertTree(root.right);

        return root;
    }
}
