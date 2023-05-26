# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dicti={}
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        print(root.val)
        def le(root,i,k):
            if root:
                if i in self.dicti.keys():
                    self.dicti[i]+=root.val
                else:
                    self.dicti[i]=root.val
                
                
                print(root.val,i)
                le(root.left,i+1,k)
                le(root.right,i+1,k)
        le(root,1,k)
        sotidict=list(sorted(self.dicti.items(),key=lambda x:x[1],reverse=True))
        print(sotidict)
        self.dicti.clear()
        if len(sotidict)>=k:
            return sotidict[k-1][1]
        else:
            return -1
     