# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:        
        inorderMap = {}
        for i, val in enumerate(inorder):
            inorderMap[val] = i
        
        self.preI = 0
        def build(l, r):
            if l > r:
                return None
            rootval = preorder[self.preI]
            self.preI += 1

            mid = inorderMap[rootval]

            node = TreeNode(rootval)
            node.left = build(l, mid - 1)
            node.right = build(mid+1, r)
            
            return node


        return build(0, len(preorder)-1)
            

            