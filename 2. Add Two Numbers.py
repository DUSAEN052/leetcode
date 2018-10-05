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
        n1, n2 = [], []
        
        while l1:
            n1.append(str(l1.val))
            l1 = l1.next
        
        while l2:
            n2.append(str(l2.val))
            l2 = l2.next
        
        total = int("".join(n1[::-1])) + int("".join(n2[::-1]))
        w = [int(t) for t in str(total)]
        node = ListNode(w.pop())
        output = node
        
        while w:
            node.next = ListNode(w.pop())
            node = node.next
        
        return output
