class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def find(s, t):
            sames = False
            if not s or not t:
                return False
            if s.val == t.val:
                sames = same(s,t)
            return sames or find(s.left, t) or find(s.right, t)
            
        def same(s, t):
            if not s and not t:
                return True
            elif not t or not s:
                return False
            return s.val == t.val and same(s.left, t.left) and same(s.right, t.right)

        return find(s, t)
