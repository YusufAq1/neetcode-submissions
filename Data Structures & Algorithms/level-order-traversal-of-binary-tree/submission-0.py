# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        level_order = []
        
        queue = [root]
        
        while queue:
            level = []
            n = len(queue)
            i = 0
            while i < n:
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
            level_order.append(level)
        
        return level_order
        
    
            

        