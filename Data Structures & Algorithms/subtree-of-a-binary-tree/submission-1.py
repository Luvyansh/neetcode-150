# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(root, subRoot, mustEqual):
            if root == None and subRoot == None:
                return True
            
            if root == None or subRoot == None:
                return False
            
            if mustEqual and root.val != subRoot.val:
                return False
            
            curr = False
            if root.val == subRoot.val:
                l = same(root.left, subRoot.left, True)
                r = same(root.right, subRoot.right, True)
                curr = l and r
            
            return curr or same(root.left, subRoot, False) or same(root.right, subRoot, False)
        return same(root, subRoot, False)