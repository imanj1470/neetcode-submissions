# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([root] if root else [])
        maxDepth = 0

        while queue:
            queueSize = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            maxDepth += 1
        return maxDepth

        #bfs with time complexity o(n) as it traversers all nodes atleast once, and cost of traversal os o(1) as using deque for o(1) inserts/popping
        #space of o(n) as storing the current row in mem
            
        