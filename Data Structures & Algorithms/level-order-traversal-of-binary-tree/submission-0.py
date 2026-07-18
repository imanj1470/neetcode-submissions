# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        res = []
        while queue:
            level = []
            queueLen = len(queue)
            for _ in range(0, queueLen):
                item = queue.pop(0)
                if not item: break
                level.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            if level: res.append(level)
        return res
    
