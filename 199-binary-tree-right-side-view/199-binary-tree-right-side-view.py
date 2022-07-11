# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        
        if not root:
            return res
        q=[root]
        
        while len(q)!=0:
            
            level_size=len(q)
            for i in range(level_size):
                node=q.pop(0)
                
                if i==level_size-1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return res