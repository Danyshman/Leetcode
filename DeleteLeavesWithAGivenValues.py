def removeLeafNodes(self, root, target):
    def dfs(node, target):
        if not node:
            return None
        node.left = dfs(node.left, target)
        node.right = dfs(node.right, target)
        if not node.left and not node.right and node.value == target:
            return None
        return node
