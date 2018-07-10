"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = Queue.Queue()
        level_map = {root:1}
        queue.put(root)
        while queue:
            node= queue.get()
            if not node:
                continue
            elif not node.left and not node.right:
                return level_map[node]
            queue.put(node.left)
            queue.put(node.right)
            level_map[node.left] = level_map[node.right] = level_map[node] + 1