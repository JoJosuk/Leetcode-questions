# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        def check(root1,root2):
            
            if root1==None or root2==None:
                return root1==root2
            return (root1.val == root2.val) and check(root1.left,root2.right) and check(root1.right,root2.left)
        return check(root.left,root.right)
hey=Solution()
print(hey.isSymmetric(TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))))

            
