# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        def inOrder(node):
            if node is None:
                return

            nonlocal count

            if node.left:
                inOrder(node.left)

            count -= 1
            if count == 0:
                smallest = node.val
                raise ValueError(node.val)

            if node.right:
                inOrder(node.right)

        try:
            inOrder(root)
        except ValueError as e:
            return int(str(e))