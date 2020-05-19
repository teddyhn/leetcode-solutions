# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
            
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
            
        if root.left is not None:
            left = 1 + self.maxDepth(root.left)
        else:
            left = 0
            
        if root.right is not None:
            right = 1 + self.maxDepth(root.right)
        else:
            right = 0
            
        return max(left, right)