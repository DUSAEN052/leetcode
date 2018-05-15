# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = ListNode(None)
        copy = output
        
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        
        while l1 and l2:
            if l1.val <= l2.val:
                output.next = l1
                l1 = l1.next
            else:
                output.next = l2
                l2 = l2.next
            
            output = output.next
        
        if l1 and not l2:
            output.next = l1
        if l2 and not l1:
            output.next = l2
        
        return copy.next
