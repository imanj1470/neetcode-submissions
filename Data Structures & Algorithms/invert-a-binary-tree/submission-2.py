# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: #bfs, and swap left/right pointers
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current is None: break
            temp = current.left
            current.left = current.right
            current.right = temp

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)
        
        return root         

        