class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # brute force, bad solution
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            return 1 + max(height(root.left), height(root.right))

        if not root:
            return True

        left = height(root.left)
        right = height(root.right)

        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)



        
        