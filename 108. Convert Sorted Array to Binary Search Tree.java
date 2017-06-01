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
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) {
            return null;
        }
        TreeNode output = bst(nums, 0, nums.length - 1);
        
        return output;
    }
    
    public TreeNode bst(int[] nums, int curr, int end) {
        int mid = (end + curr)/2;
        
        if (curr > end) {
            return null;
        }
        TreeNode root = new TreeNode(nums[mid]);
        root.left = bst(nums, curr, mid - 1);
        root.right = bst(nums, mid + 1, end);
        
        return root;
    }
}
