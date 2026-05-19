# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        # Base case
        if not root or root == p or root == q:
            return root

        # Search in left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search in right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return nodes, root is LCA
        if left and right:
            return root

        # Otherwise return non-null side
        return left if left else right