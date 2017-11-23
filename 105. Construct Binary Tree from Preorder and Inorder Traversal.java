/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0 && inorder.length == 0) {
            return null;
        }
        
        TreeNode output = new TreeNode(preorder[0]);
        int index = 0;
        
        for (int i = 0; i < inorder.length; i++) {
            if(inorder[i] == output.val) {
                index = i;
                break;
            }
        }
        
        int[] inorderLeft = new int[0];
        int[] inorderRight = new int[0];
        int[] preorderLeft = new int[0];
        int[] preorderRight = new int[0];
        
        if (index > 0) {
            inorderLeft = Arrays.copyOfRange(inorder, 0, index);
        }
        if (index + 1 < inorder.length) {
            inorderRight = Arrays.copyOfRange(inorder, index + 1, inorder.length);
        }
        if (inorderLeft.length + 1 > 1) {
            preorderLeft = Arrays.copyOfRange(preorder, 1, inorderLeft.length + 1);
        }
        if (preorder.length > inorderLeft.length + 1) {
            preorderRight = Arrays.copyOfRange(preorder, inorderLeft.length + 1, preorder.length);
        }
        
        output.left = buildTree(preorderLeft, inorderLeft);
        output.right = buildTree(preorderRight, inorderRight);
        
        return output;
        
    }
}
