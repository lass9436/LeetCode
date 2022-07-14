# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root=TreeNode(preorder.pop(0))
        root_idx=inorder.index(root.val)
        root.left=self.buildTree(preorder,inorder[:root_idx])
        root.right=self.buildTree(preorder,inorder[root_idx+1:])
        return root