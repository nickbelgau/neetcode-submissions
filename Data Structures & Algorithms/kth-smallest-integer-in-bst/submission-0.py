# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # use inorder traversal (left, node, right) to traverse in ascending order
        # rebuild it as an array, more clear, but uses more space
        values = []
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        dfs(root)
        return values[k - 1]