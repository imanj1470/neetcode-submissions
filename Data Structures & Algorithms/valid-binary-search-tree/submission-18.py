# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkTree(node, lower, upper):
            if node is None:
                print("Null node, ret false")
                return False
            

            print("Current:", node.val, "lower/upper", lower, upper)

            responseL = None   
            responseR = None     

            if node.val <= lower:
                print(f"invalid, current: {node.val} < {lower} (lowest)")
                return False
            elif node.val >= upper:
                print(f"invalid, current: {node.val} > {lower} (highest)")
                return False


            if not (node.right or node.left):
                print("base case (leaf), returning true")
                return True


            if node.left:
                print("going left")
                responseL = node.left.val < node.val and checkTree(node.left, lower, min(upper, node.val))
            if node.right:
                print("going right")
                responseR = node.right.val > node.val and checkTree(node.right, max(lower, node.val), upper)

            print("returning res,", responseL, responseR)
            if responseL is not None and responseR is not None:
                return responseL and responseR
            elif responseL is not None:
                return responseL
            elif responseR is not None:
                return responseR
            
        res = checkTree(root, -1001, 1001)
        return res
            
        