# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        def depthfinder(node,count):
            if not node:
                return count
            count+=1
            return max(depthfinder(node.left,count),depthfinder(node.right,count))
        return depthfinder(root,0)
    def maxDepth2(self, root) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
hey = Solution()
print(hey.maxDepth(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))))
print(hey.maxDepth2(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))))
