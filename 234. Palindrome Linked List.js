/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let stack = [];
    let ln = head
    
    while (ln) {
        stack.push(ln.val);
        ln = ln.next;
    }
    if (stack.length == 1) {
        return true;
    }
    while (head) {
        if (head.val != stack[stack.length - 1]) {
            return false;
        }
        head = head.next;
        stack.pop();
    }
    return true;
};
