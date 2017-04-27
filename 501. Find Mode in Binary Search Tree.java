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
    HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
    public int[] findMode(TreeNode root) {
        int max = 0;
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) {
            return new int[0];
        }
        inorder(root);
        for (Integer i : hm.values()) {
            if (i > max) {
                max = i;
            }
        }
        for (Map.Entry<Integer, Integer> entry : hm.entrySet()) {
            Integer key = entry.getKey();
            Integer val = entry.getValue();
            if (val == max) {
                res.add(key);
            }
        }
        int[] output = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            output[i] = res.get(i);
        }
        return output;
    }
    public void inorder(TreeNode root) {
        if (root != null) {
            inorder(root.left);
            if (hm.containsKey(root.val)) {
                hm.put(root.val, hm.get(root.val) + 1);
            } else {
                hm.put(root.val, 1);
            }
            
            inorder(root.right);
        }
    }
}
