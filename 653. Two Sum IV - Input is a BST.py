class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        elements = []
        
        def getElements(root, elements):
            if root:
                elements.append(root.val)
                if root.left:
                    getElements(root.left, elements)
                if root.right:
                    getElements(root.right, elements)
    
        getElements(root, elements)
        
        for i in range(len(elements)):
            target = k - elements[i]
            for j in range(i + 1, len(elements)):
                if elements[j] == target:
                    return True
        return False
