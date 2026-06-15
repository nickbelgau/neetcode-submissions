# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        # If this is a leaf, check the sum directly
        if root.left is None and root.right is None:
            return root.val == targetSum
        # Keep looking in the left and right subtrees
        remaining = targetSum - root.val # this becomes the target sum of subtree
        if self.hasPathSum(root.left, remaining):
            return True
        if self.hasPathSum(root.right, remaining):
            return True
        return False
        # return (
        #     self.hasPathSum(root.left, remaining)
        #     or self.hasPathSum(root.right, remaining)
        # )