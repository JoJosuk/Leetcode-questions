#
# @lc app=leetcode id=1646 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss=1
        for i in arr:
            while i>miss:
                miss+=1
                k-=1
                if k==0:
                    return miss-1
            miss=i+1
        while 1:
            miss+=1
            k-=1
            if k==0:
                return miss-1


        
        
# @lc code=end

