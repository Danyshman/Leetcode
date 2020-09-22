# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root) -> int:
        ans = (root.val, 0)
        def dfs(node, depth):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right and depth > ans[1]:
                    ans = (node.val, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return ans[0]