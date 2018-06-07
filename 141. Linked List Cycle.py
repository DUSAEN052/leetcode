# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        s = head
        f = head
        
        while f and f.next:
            s = s.next
            f = f.next.next
            
            if s is f:
                return True
        
        return False
