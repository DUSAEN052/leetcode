/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode output = null;
        Set<ListNode> mySet = new HashSet<>();
        
        while (headA != null) {
            mySet.add(headA);
            headA = headA.next;
        }
        
        while (headB != null) {
            if (mySet.contains(headB)) {
                return headB;
            }
            headB = headB.next;
        }
        
        return output;
    }
}