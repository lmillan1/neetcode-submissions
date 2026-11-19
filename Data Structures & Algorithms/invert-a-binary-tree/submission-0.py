# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        while queue:
            # pop the left
            current = queue.popleft()

            # swap children
            current.left, current.right = current.right, current.left

            # add existing children in queue
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root



        