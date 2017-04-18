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
    List<Integer> lst = new ArrayList<Integer>();
    public List<Integer> preorderTraversal(TreeNode root) {
        preorder(root);
        return lst;
    }
    
    public void preorder(TreeNode root) {
        if(root != null) {
            lst.add(root.val);
            preorder(root.left);
            preorder(root.right);
        }
    }
}
