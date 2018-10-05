# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        
        n1, n2 = [], []
        
        while l1:
            n1.append(str(l1.val))
            l1 = l1.next
        
        while l2:
            n2.append(str(l2.val))
            l2 = l2.next
        
        total = int("".join(n1)) + int("".join(n2))
        w = [n for n in str(total)]
        node = ListNode(w.pop(0))
        output = node
        
        while w:
            node.next = ListNode(w.pop(0))
            node = node.next
        
        return output
