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
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) {
            return null;
        }
        TreeNode node = move(t1, t2);
        return node;
    }
    
    public TreeNode move(TreeNode t1, TreeNode t2) {
        int val = 0;
        
        if (t1 == null && t2 == null) {
            return null;
        }
        
        if (t1 == null && t2 != null) {
            val = t2.val;
        } else if (t2 == null && t1 != null) {
            val = t1.val;
        } else {
            val = t1.val + t2.val;
        }
        
        TreeNode root = new TreeNode(val);
        
        if (t1 == null) {
            root.left = move(null, t2.left);
            root.right = move(null, t2.right);
        } else if (t2 == null) {
            root.left = move(t1.left, null);
            root.right = move(t1.right, null);
        } else {
            root.left = move(t1.left, t2.left);
            root.right = move(t1.right, t2.right);
        }
        
        
        return root;
    }
}
