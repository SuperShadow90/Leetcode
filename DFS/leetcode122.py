
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        This is the recursion way
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
    
        if not root.left and not root.right and (sum - root.val == 0):
            return True
        
        print root.val, sum
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)