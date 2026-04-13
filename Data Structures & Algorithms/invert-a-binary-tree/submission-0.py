class Solution:
    def preOrder(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return        
        root.left, root.right = root.right, root.left
        self.preOrder(root.left)
        self.preOrder(root.right)
        return root
    
    def bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        return self.bfs(root)