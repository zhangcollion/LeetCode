# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = [(root, 0)]
        ans = 0
        while queue:
            n = len(queue)
            tmp = []
            for i in range(n):
                node, level = queue.pop(0)
                tmp.append(level)
                if node.right:
                    queue.append((node.right,2*level+1))
                if node.left:
                    queue.append((node.left, 2*level+0))
            ans = max(max(tmp)-min(tmp)+1, ans)
        return ans