# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        out = ListNode(0)
        curr = out
        nxt = head
        
        while nxt and nxt.next:
            if nxt.val == nxt.next.val:
                while nxt.next and nxt.val == nxt.next.val:
                    nxt = nxt.next
                
                nxt = nxt.next
            else:
                curr.next = nxt
                curr = curr.next
                nxt = nxt.next 
            
            curr.next = nxt
        
        return out.next
 