#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        suffix=[1]*length
        prefix=[1]*length
        suffix[0]=1
        for i in range(1,len(nums)):
            suffix[i]=(nums[i-1]*suffix[i-1])
        prefix[-1]=1
        for i in range(len(nums)-2,-1,-1):
            prefix[i]=(nums[i+1]*prefix[i+1])
        for i in range(len(nums)):
            prefix[i]=prefix[i]*suffix[i]
        return prefix        
# @lc code=end

