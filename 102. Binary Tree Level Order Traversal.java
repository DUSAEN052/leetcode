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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        Queue<TreeNode> q1 = new LinkedList<>();
        Queue<TreeNode> q2 = new LinkedList<>();
        
        if (root == null) {
            return output;
        }
        
        q1.add(root);
        
        while (!q1.isEmpty() || !q2.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            while(!q1.isEmpty()) {
                root = q1.poll();
                level.add(root.val);
                if (root.left != null) {
                    q2.add(root.left);
                }
                if (root.right != null) {
                    q2.add(root.right);
                }
            }
            if (level.size() > 0) {
                output.add(level);
            }
            level = new ArrayList<>();
            
            while (!q2.isEmpty()) {
                root = q2.poll();
                level.add(root.val);
                if (root.left != null) {
                    q1.add(root.left);
                }
                if (root.right != null) {
                    q1.add(root.right);
                }
            }
            if (level.size() > 0) {
                output.add(level);
            }
            level = new ArrayList<>();
        }
        
        return output;
    }
}
