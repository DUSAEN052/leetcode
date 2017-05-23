/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode output = null;
        
        if (head == null) {
            return head;
        } else {
            while (head != null) {
                ListNode nxt = head.next; // save next 
                head.next = output; // next is now the previous
                output = head; // moved previous into current
                head = nxt; // move head onto next
            }
        }
        return output;
    }
}
