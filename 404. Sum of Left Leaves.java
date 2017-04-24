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
    public int sumOfLeftLeaves(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<TreeNode> current = new LinkedList<>();
        Queue<TreeNode> children = new LinkedList<>();
        int sum = 0;
        current.add(root);
        
        while (!current.isEmpty()) {
            for (TreeNode n : current) {
                if (n.left != null) {
                    children.add(n.left);
                    sum += n.left.val;
                    if (n.left.left != null || n.left.right != null) {
                        sum -= n.left.val;
                    }
                }
                if (n.right != null) {
                    children.add(n.right);
                }
            }
            
            current = children;
            children = new LinkedList<>();
        }
        
        return sum;
    }
}
