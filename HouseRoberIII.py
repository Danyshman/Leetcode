def rob(root):
    dp = {}

    def dfs(node, parent):
        if node in dp:
            return dp[node]
        if not root:
            return 0
        if parent:
            return dfs(node.left, node.right, False)
        temp = max(node.val + dfs(node.left, node.right, True), dfs(node.left, node.right, False))
        dp[node] = temp
        return temp
    return dfs(root, False)
