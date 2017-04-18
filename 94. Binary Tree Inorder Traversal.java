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
    List<Integer> output = new ArrayList<Integer>();
    public List<Integer> inorderTraversal(TreeNode root) {
        inorder(root);
        
        return output;
    }
    
    public void inorder(TreeNode root) {
        if (root != null) {
            inorder(root.left);
            output.add(root.val);
            inorder(root.right);
        }
    }
}
