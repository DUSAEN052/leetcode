# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        output = None
        
        if not head:
            return head
        
        while head:
            tmp = head.next
            head.next = output
            output = head
            head = tmp
        
        return output
