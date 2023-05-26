#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        while l<r:
            currsum =nums[l]+nums[r] 
            if currsum>target:
                r-=1
            elif currsum<target:
                l+=1
            else: return [l+1,r+1]


        
# @lc code=end

