/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
let deleteDuplicates = function(head) {
    let ln = head;
    while (ln) {
        if (ln.next && ln.val == ln.next.val) {
            ln.next = ln.next.next;
        } else {
            ln = ln.next;
        }
    }
    return head;
};
