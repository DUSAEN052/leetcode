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
    List<Integer> nums = new ArrayList<Integer>();
    public int getMinimumDifference(TreeNode root) {
        findNumbers(root);
        Collections.sort(nums);
        int min = nums.get(nums.size() - 1);
        for (int i = 0; i < nums.size() - 1; i++) {
            if (Math.abs(nums.get(i) - nums.get(i+1)) < min) {
                min = Math.abs(nums.get(i) - nums.get(i+1));
            }
        }
        return min;
        
    }
    public void findNumbers(TreeNode root) {
        if (root != null) {
            nums.add(root.val);
            findNumbers(root.left);
            findNumbers(root.right);
        }
    }
}
