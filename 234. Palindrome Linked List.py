# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        contents = []
        
        while head:
            contents.append(head.val)
            head = head.next
        
        return contents == contents[::-1]
