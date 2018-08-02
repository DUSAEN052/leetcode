# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        gset = set()
        count = 0
        
        for g in G:
            gset.add(g)
        
        while head:
            if head.val in gset:
                count += 1
                
                while head and head.val in gset:
                    head = head.next
            else:
                head = head.next
        
        return count
