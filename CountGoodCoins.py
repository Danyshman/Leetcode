# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, parentMax):
            nonlocal count
            if not node:
                return
            if parentMax <= node.val:
                count += 1
            dfs(node.left, max(node.val, parentMax))
            dfs(node.right, max(node.val, parentMax))
        dfs(root, -10001)
        return count