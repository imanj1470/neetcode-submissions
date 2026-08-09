# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def searchTree(nodeA, nodeB):
            if not nodeA and not nodeB:
                return True
            elif not nodeA or not nodeB:
                return False
            print(nodeA.val, nodeB.val)

            if nodeA.val != nodeB.val:
                print("NO MATCH")
                return False

            return searchTree(nodeA.left, nodeB.left) and searchTree(nodeA.right, nodeB.right)


        res = searchTree(p,q)
        if res is False:
            return False
        else:
            return True