# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):


# Iterative Method 
    def inorderTraversal(self, root):
        res = []
        stack = []
        cur = root

        # loop running till cur or stack is not Null
        while cur or stack:

            # loop until cur is not Null
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur)
            cur = cur.right


# Recursive Method
            # Recursively calls the InOrder function for traversal
            def inorder(root):
                inorder(root.left)
                res.append(root.val) 
                inorder(root.right)
            inorder(root)
            return res
        