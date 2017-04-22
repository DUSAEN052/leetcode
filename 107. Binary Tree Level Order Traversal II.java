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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        if (root == null) {
            return output;
        }
        Queue<TreeNode> q1 = new LinkedList<>();
        Queue<TreeNode> q2 = new LinkedList<>();
        q1.add(root);
        while (!q1.isEmpty() || !q2.isEmpty()) {
            List<Integer> l1 = new ArrayList<Integer>();
            while (!q1.isEmpty()) {
                root = q1.poll();
                l1.add(root.val);
                if (root.left != null) {
                    q2.add(root.left);
                }
                if (root.right != null) {
                    q2.add(root.right);
                }
            }
            if (l1.size() > 0) {
                output.add(l1);
            }
            List<Integer> l2 = new ArrayList<Integer>();
            while (!q2.isEmpty()) {
                root = q2.poll();
                l2.add(root.val);
                if (root.left != null) {
                    q1.add(root.left);
                }
                if (root.right != null) {
                    q1.add(root.right);
                }
            }
            if (l2.size() > 0){
                output.add(l2);
            }
        }
       Collections.reverse(output);
       return output;
    }
}
