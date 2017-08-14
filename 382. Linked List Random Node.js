/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
 * @param {ListNode} head
 */
let Solution = function(head) {
    this.head = head
};

/**
 * Returns a random node's value.
 * @return {number}
 */
Solution.prototype.getRandom = function() {
    let n = this.head
    let r = n.val
    
    for (let i = 1; n.next !== null; i++) {
        n = n.next
        let ran = Math.floor(Math.random() * (i + 1))
        
        if (ran == i) {
            r = n.val
        }
    }
    return r
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = Object.create(Solution).createNew(head)
 * var param_1 = obj.getRandom()
 */
 
 