# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        fc = 0
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            fc += 2
        
        if fc % 2 != 0:
            return slow.next
        else:
            return slow
