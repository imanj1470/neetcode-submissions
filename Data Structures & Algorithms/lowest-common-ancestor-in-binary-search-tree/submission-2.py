# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        minInput = min(p.val,q.val)
        maxInput = max(p.val,q.val)

        current = root
        while current:
            if maxInput < current.val:
                current = current.left
            elif minInput > current.val:
                current = current.right
            else: #as diverginb
                return current



                        
                    


        