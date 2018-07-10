"""
Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
We are hoping to solve this problem both recursively and iteratively.
"""
class Solution(object):
	"""
	This is a recursive solution.

	Two trees are only mirror of each other when left child of the left tree is a 
	mirror of the right child of the right tree, etc.
	So we devide the problem into a smaller problem by applying recursion.
	"""
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)


    def isMirror(self, n1, n2):
        if not n1 and not n2:
            return True
        elif not n1 or not n2:
            return False
    	if n1.val != n2.val:
    		return False
    	return self.isMirror(n1.right, n2.left) and self.isMirror(n1.left, n2.right)


class Solution(object):
	"""
	This is a iterative solution.
	"""
	 def isSymmetric(self, root):
	 	 queue = []
	 	 queue.add(root)
	 	 queue.add(root)
	 	 while queue:
	 	 	n1 = queue.pop(0)
	 	 	n2 = queue.pop(0)
	 	 	if not n1 and not n2:
            	continue
            # I messed up the above logic initially. 
            # if we return true above, this algorithm will end too early.
        	elif not n1 or not n2:
            	return False
            elif n1.val != n2.val:
    			return False
    		queue.add(n1.left)
    		queue.add(n2.right)
    		queue.add(n1.right)
    		queue.add(n2.left)
    	return True


