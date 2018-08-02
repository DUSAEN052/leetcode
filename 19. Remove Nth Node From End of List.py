# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None or n == 0:
            return head
        
        out = ListNode(0)
        slow = head
        fast = head
        count = 0
        start = 0
        out.next = slow
        
        while fast:
            fast = fast.next
            count += 1
        
        if n == count:
            out.next = slow.next
            return out.next
        
        while count - n != start + 1 and slow:
            start += 1
            slow = slow.next
        
        slow.next = slow.next.next
        
        return out.next
