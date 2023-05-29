import webbrowser
# Definition for a binary tree node.
url='https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/'
webbrowser.open(url, new=2)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def printtree(self):
        def printtreehelper(node):
            if not node:
                return
            print(node.val)
            printtreehelper(node.left)
            printtreehelper(node.right)
        printtreehelper(self)
class Solution:
        
    def sortedArrayToBST(self, nums) :
        no=len(nums)
        mid=no//2
        if not no:
            return None
        return(
            TreeNode(nums[mid],self.sortedArrayToBST(nums[:mid]),self.sortedArrayToBST(nums[mid+1:]))
        )
        
hey=Solution()
a=hey.sortedArrayToBST([-10,-3,0,5,9])
a.printtree()