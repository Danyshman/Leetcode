# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root):
        ans = []
        def dfs(node, depth):
            if not node:
                return
            if len(ans) < depth:
                ans.append(node.val)
            elif len(ans) >= depth:
                ans[depth-1] = max(node.val, ans[depth-1])
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 1)
        return ans