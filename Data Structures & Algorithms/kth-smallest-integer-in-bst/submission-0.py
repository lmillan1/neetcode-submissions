# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            # go far as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # process leftmost node
            curr = stack.pop()
            k -= 1

            # check if smallest element
            if k == 0:
                return curr.val
            curr = curr.right

        